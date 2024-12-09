from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(100), nullable=False)
    contactNo = Column(String(15), nullable=False)
    cgpa = Column(Float, nullable=False)
    course = Column(String(100), nullable=False)
