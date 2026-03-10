from .database import session, Student

def get_students():
    students = session.query(Student).all()
    return students