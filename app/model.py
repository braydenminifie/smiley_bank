from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///orm.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    name = Column(String)
    smiles = Column(Integer)

    def __init__(self, student_id: int, name: str, smiles: int):
        self.student_id = student_id
        self.name = name
        self.smiles = smiles


Base.metadata.create_all(engine)

