from .database import session, Student, Prize

def get_students():
    students = session.query(Student).all()
    return students

def get_student_by_id(id: int):
    student = session.query(Student).filter(Student.student_id == id)
    return student

def add_student(student: Student):
    session.merge(student)
    session.commit()

def remove_student_by_id(id: int):
    print(f"removing student with id {id}")
    student = session.query(Student).filter(Student.student_id == id).first()
    session.delete(student)
    session.commit()

def add_smiles(student_id: int, smiles: int):
    student = session.query(Student).get(student_id)
    student.smiles += smiles
    session.commit()
    print("added a smile")
    

def remove_smiles(student_id: int, smiles: int):
    student = session.query(Student).get(student_id)
    student.smiles -= smiles
    session.commit()

def get_prizes():
    prizes = session.query(Prize).all()
    return prizes

def add_prize(prize: Prize):
    session.merge(prize)
    session.commit()

def remove_prize(id: int):
    prize = session.query(Prize).filter(Prize.prize_id == id).first()
    session.delete(prize)
    session.commit()
