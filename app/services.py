from .database import session, Student, Prize, History
from datetime import datetime

def get_students():
    students = session.query(Student).all()
    return students

def get_student_by_id(id: int):
    student = session.query(Student).filter(Student.student_id == id)
    return student

def add_student(student: Student):
    session.add(student)
    session.commit()


def remove_student_by_id(id: int):
    student = session.query(Student).filter(Student.student_id == id).first()
    session.delete(student)
    session.commit()

    history = History(None, student.student_id, get_date(), student.name, "Profile Removed", None)
    add_history(history)

def add_smiles(student_id: int, smiles: int):
    student = session.query(Student).get(student_id)
    student.smiles += smiles
    session.commit()
    

def remove_smiles(student_id: int, smiles: int):
    student = session.query(Student).get(student_id)
    student.smiles -= smiles
    session.commit()


def get_prizes():
    prizes = session.query(Prize).all()
    return prizes

def add_prize(prize: Prize):
    session.add(prize)
    session.commit()

def remove_prize(id: int):
    prize = session.query(Prize).filter(Prize.prize_id == id).first()
    session.delete(prize)
    session.commit()

def add_history(history: History):
    potential_entry = session.query(History).filter(
        History.student_id == history.student_id,
        History.date == history.date,
        History.action == history.action
    ).first()

    
    if potential_entry:
        potential_entry.points += history.points
        session.commit()
        return potential_entry

    else:
        session.add(history)
        session.commit()
        return history
    

def get_history():
    history = session.query(History).all()
    return history

def get_date():
    today = datetime.now().strftime("%d/%m/%Y")
    return today

