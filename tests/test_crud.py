import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database.models as models
import database.schemas as schemas
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
        models.Base.metadata.drop_all(bind=engine) 

def test_create_student(db):
    student = schemas.StudentCreate(name="Luke", email="luke@gmail.com", address="Kandy", contactNo="0771234567", cgpa=3.77)
    db_student = crud.create_student(db, student)
    assert db_student.name == "Luke"
    assert db_student.email == "luke@gmail.com"

def test_get_student(db):
    student = schemas.StudentCreate(name="Lukes", email="luke2@gmail.com", address="Kandy", contactNo="0771234567", cgpa=3.77)
    db_student = crud.create_student(db, student)
    fetched_student = crud.get_student(db, db_student.id)
    assert fetched_student.id == db_student.id

def test_get_students(db):
    students = crud.get_students(db)
    assert len(students) > 0

def test_delete_student(db):
    student = schemas.StudentCreate(name="luke", email="lukes@gmail.com", address="Kandy", contactNo="0771234567", cgpa=3.77)
    db_student = crud.create_student(db, student)
    deleted_student = crud.delete_student(db, db_student.id)
    assert deleted_student.id == db_student.id
