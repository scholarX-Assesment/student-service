import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import models, schemas
from api import crud

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_student(db):
    student = schemas.StudentCreate(name="John Doe", age=20)
    db_student = crud.create_student(db, student)
    assert db_student.name == "John Doe"
    assert db_student.age == 20

def test_get_student(db):
    student = schemas.StudentCreate(name="Jane Doe", age=22)
    db_student = crud.create_student(db, student)
    fetched_student = crud.get_student(db, db_student.id)
    assert fetched_student.id == db_student.id

def test_get_students(db):
    students = crud.get_students(db)
    assert len(students) >= 0

def test_delete_student(db):
    student = schemas.StudentCreate(name="Mark Smith", age=21)
    db_student = crud.create_student(db, student)
    deleted_student = crud.delete_student(db, db_student.id)
    assert deleted_student.id == db_student.id

def test_create_academic_history(db):
    student = schemas.StudentCreate(name="Alice Johnson", age=23)
    db_student = crud.create_student(db, student)
    academic = schemas.AcademicHistoryCreate(course_name="Math", grade="A")
    db_academic = crud.create_academic_history(db, academic, db_student.id)
    assert db_academic.course_name == "Math"
    assert db_academic.grade == "A"

def test_get_academic_history(db):
    student = schemas.StudentCreate(name="Bob Brown", age=24)
    db_student = crud.create_student(db, student)
    academic = schemas.AcademicHistoryCreate(course_name="Science", grade="B")
    crud.create_academic_history(db, academic, db_student.id)
    academic_history = crud.get_academic_history(db, db_student.id)
    assert len(academic_history) > 0

def test_create_course(db):
    course = schemas.CourseCreate(name="Physics", description="Physics course")
    db_course = crud.create_course(db, course)
    assert db_course.name == "Physics"
    assert db_course.description == "Physics course"

def test_get_course(db):
    course = schemas.CourseCreate(name="Chemistry", description="Chemistry course")
    db_course = crud.create_course(db, course)
    fetched_course = crud.get_course(db, db_course.id)
    assert fetched_course.id == db_course.id

def test_get_courses(db):
    courses = crud.get_courses(db)
    assert len(courses) >= 0

def test_enroll_student_in_course(db):
    student = schemas.StudentCreate(name="Charlie Green", age=25)
    db_student = crud.create_student(db, student)
    course = schemas.CourseCreate(name="Biology", description="Biology course")
    db_course = crud.create_course(db, course)
    enrollment = crud.enroll_student_in_course(db, db_student.id, db_course.id)
    assert enrollment.student_id == db_student.id
    assert enrollment.course_id == db_course.id

def test_get_student_courses(db):
    student = schemas.StudentCreate(name="Diana White", age=26)
    db_student = crud.create_student(db, student)
    course = schemas.CourseCreate(name="History", description="History course")
    db_course = crud.create_course(db, course)
    crud.enroll_student_in_course(db, db_student.id, db_course.id)
    student_courses = crud.get_student_courses(db, db_student.id)
    assert len(student_courses) > 0
