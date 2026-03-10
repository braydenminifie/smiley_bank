from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, declarative_base

engine = create_engine('sqlite:///orm.db')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    name = Column(String)
    smiles = Column(Integer)
    bank_colour = Column(String)

    def __init__(self, student_id: int, name: str, smiles: int, bank_colour: str):
        self.student_id = student_id
        self.name = name
        self.smiles = smiles
        self.bank_colour = bank_colour

    def __repr__(self):
        return f"({self.student_id}, {self.name}, {self.smiles}, {self.bank_colour})"


def init_db():
    Base.metadata.create_all(engine)

