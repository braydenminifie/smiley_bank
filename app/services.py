from .database import session, Student

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