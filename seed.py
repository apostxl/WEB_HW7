from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Subject, Teacher, Grade, Base

# Підключення до бази даних
engine = create_engine('sqlite:///students.db')
Base.metadata.bind = engine

# Створення сесії
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Ініціалізація Faker для створення випадкових даних
fake = Faker()

# Функція для створення студентів
def create_students(num_students):
    for _ in range(num_students):
        student = Student(name=fake.name(), email=fake.email())
        session.add(student)
    session.commit()

# Функція для створення груп
def create_groups(num_groups):
    for i in range(1, num_groups + 1):
        group = Group(name=f'Group {i}')
        session.add(group)
    session.commit()

# Функція для створення предметів
def create_subjects(num_subjects):
    for _ in range(num_subjects):
        subject = Subject(name=fake.word())
        session.add(subject)
    session.commit()

# Функція для створення викладачів
def create_teachers(num_teachers):
    for _ in range(num_teachers):
        teacher = Teacher(name=fake.name())
        session.add(teacher)
    session.commit()

# Функція для створення оцінок
def create_grades(num_grades):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    teachers = session.query(Teacher).all()

    for _ in range(num_grades):
        student = fake.random_element(students)
        subject = fake.random_element(subjects)
        teacher = fake.random_element(teachers)
        grade = Grade(
            student_id=student.id,
            subject_id=subject.id,
            teacher_id=teacher.id,
            score=fake.random_int(min=1, max=100)
        )
        session.add(grade)
    session.commit()

if __name__ == '__main__':
    create_students(50)
    create_groups(3)
    create_subjects(8)
    create_teachers(5)
    create_grades(20)
