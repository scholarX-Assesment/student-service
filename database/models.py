from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from database.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(500), nullable=True)
    credits = Column(Float, nullable=False)

    enrolled_students = relationship("EnrolledCourse", back_populates="course")


class EnrolledCourse(Base):
    __tablename__ = "enrolled_courses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)

    student = relationship("Student", back_populates="enrolled_courses")
    course = relationship("Course", back_populates="enrolled_students")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(100), nullable=False)
    contactNo = Column(String(15), nullable=False)
    cgpa = Column(Float, nullable=False)

    academic_history = relationship("AcademicHistory", back_populates="student", cascade="all, delete-orphan")
    enrolled_courses = relationship("EnrolledCourse", back_populates="student", cascade="all, delete-orphan")


class AcademicHistory(Base):
    __tablename__ = "academic_history"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    year = Column(Integer, nullable=False)
    achievement = Column(String(255), nullable=False)

    student = relationship("Student", back_populates="academic_history")
