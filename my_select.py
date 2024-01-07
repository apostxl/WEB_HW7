from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Subject, Teacher, Grade, Base

# Підключення до бази даних
engine = create_engine('sqlite:///students.db')
Base.metadata.bind = engine

# Створення сесії
DBSession = sessionmaker(bind=engine)
session = DBSession()

def select_1():
    query = session.query(Student, func.avg(Grade.score).label('avg_score')).\
        join(Grade, Student.id == Grade.student_id).\
        group_by(Student.id).\
        order_by(func.avg(Grade.score).desc()).limit(5)
    return query.all()

def select_2(subject_name):
    query = session.query(Student, func.avg(Grade.score).label('avg_score')).\
        join(Grade, Student.id == Grade.student_id).\
        join(Subject, Grade.subject_id == Subject.id).\
        filter(Subject.name == subject_name).\
        group_by(Student.id).\
        order_by(func.avg(Grade.score).desc()).limit(1)
    return query.first()

def select_3(subject_name):
    query = session.query(Group.name, func.avg(Grade.score).label('avg_score')).\
        join(Subject, Group.id == Subject.group_id).\
        join(Grade, Subject.id == Grade.subject_id).\
        filter(Subject.name == subject_name).\
        group_by(Group.name)
    return query.all()

def select_4():
    query = session.query(func.avg(Grade.score).label('avg_score'))
    return query.scalar()

def select_5(teacher_name):
    query = session.query(Subject.name).join(Teacher, Subject.teacher_id == Teacher.id).\
        filter(Teacher.name == teacher_name)
    return query.all()

def select_6(group_name):
    query = session.query(Student).join(Group, Student.group_id == Group.id).\
        filter(Group.name == group_name)
    return query.all()

def select_7(group_name, subject_name):
    query = session.query(Grade).join(Subject, Grade.subject_id == Subject.id).\
        join(Group, Subject.group_id == Group.id).\
        filter(Group.name == group_name, Subject.name == subject_name)
    return query.all()

def select_8(teacher_name):
    query = session.query(func.avg(Grade.score).label('avg_score')).\
        join(Subject, Grade.subject_id == Subject.id).\
        join(Teacher, Subject.teacher_id == Teacher.id).\
        filter(Teacher.name == teacher_name)
    return query.scalar()

def select_9(student_name):
    query = session.query(Subject.name).join(Grade, Subject.id == Grade.subject_id).\
        join(Student, Grade.student_id == Student.id).\
        filter(Student.name == student_name)
    return query.all()

def select_10(student_name, teacher_name):
    query = session.query(Subject.name).join(Grade, Subject.id == Grade.subject_id).\
        join(Teacher, Subject.teacher_id == Teacher.id).\
        join(Student, Grade.student_id == Student.id).\
        filter(Student.name == student_name, Teacher.name == teacher_name)
    return query.all()
