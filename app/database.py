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

    history = relationship("History", back_populates="student")

    def __init__(self, student_id: int, name: str, smiles: int, bank_colour: str):
        self.student_id = student_id
        self.name = name
        self.smiles = smiles
        self.bank_colour = bank_colour

    def __repr__(self):
        return f"({self.student_id}, {self.name}, {self.smiles}, {self.bank_colour})"

class Prize(Base):
    __tablename__ = 'prizes'
    prize_id = Column(Integer, Sequence('prize_id_seq'), primary_key = True)
    prize = Column(String)
    cost = Column(Integer)
    image = Column(String)

    def __init__(self, prize_id: int, prize: str, cost: int, image: str):
        self.prize_id = prize_id
        self.prize = prize
        self.cost = cost
        self.image = image

    def __repr__(self):
        return f"({self.prize_id}, {self.prize}, {self.cost}, {self.image})"


class History(Base):
    __tablename__ = 'history'
    history_id = Column(Integer, Sequence('history_id_seq'), primary_key = True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    date = Column(String)
    name = Column(String)
    action = Column(String)
    points = Column(Integer)

    student = relationship("Student", back_populates="history")

    def __init__(self, history_id: int, student_id: int, date: str, name: str, action: str, points: int):
        self.history_id = history_id
        self.student_id = student_id
        self.date = date
        self.name = name
        self.action = action
        self.points = points

    def __repr__(self):
        return f"({self.history_id}, {self.student_id}, {self.date}, {self.name}, {self.action}, {self.points})"

def init_db():
    Base.metadata.create_all(engine)

