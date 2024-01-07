from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Subject, Teacher, Grade, Base
import random
from datetime import datetime, timedelta

engine = create_engine('sqlite:///students.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

fake = Faker()

def create_students(num_students):
    for _ in range(num_students):
        student = Student(name=fake.name(), email=fake.email())
        session.add(student)
    session.commit()

def create_groups(num_groups):
    for i in range(1, num_groups + 1):
        group = Group(name=f'Group {i}')
        session.add(group)
    session.commit()

def create_subjects_and_teachers(num_subjects, num_teachers):
    teachers = []
    for _ in range(num_teachers):
        teacher = Teacher(name=fake.name())
        teachers.append(teacher)
        session.add(teacher)
    session.commit()

    for _ in range(num_subjects):
        teacher = random.choice(teachers)
        subject = Subject(name=fake.word(), teacher_id=teacher.id)
        session.add(subject)
    session.commit()

def create_grades(num_students, num_subjects):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for _ in range(num_students):
        student = random.choice(students)
        for _ in range(num_subjects):
            subject = random.choice(subjects)
            date = fake.date_time_between(start_date='-1y', end_date='now')
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                score=random.randint(1, 100),
                date_received=date
            )
            session.add(grade)
    session.commit()

if __name__ == '__main__':
    create_students(50)
    create_groups(3)
    create_subjects_and_teachers(8, 5)
    create_grades(50, 8)

