from .database import session, Student

def get_students():
    students = session.query(Student).all()
    return students

def add_student(student: Student):
    session.merge(student)
    session.commit()
