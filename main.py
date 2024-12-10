from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database.models as models
import database.schemas as schemas
import api.crud as crud
import database.database as database
from typing import List

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.get("/students/", response_model=List[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_students(db=db, skip=skip, limit=limit)

@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(database.get_db)):
    student = crud.delete_student(db=db, student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/students/{student_id}/academic-history/", response_model=schemas.AcademicHistory)
def add_academic_history(student_id: int, academic: schemas.AcademicHistoryCreate, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.create_academic_history(db, academic, student_id)

@app.get("/students/{student_id}/academic-history/", response_model=List[schemas.AcademicHistory])
def get_academic_history(student_id: int, db: Session = Depends(database.get_db)):
    return crud.get_academic_history(db, student_id)

@app.post("/courses/", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(database.get_db)):
    return crud.create_course(db=db, course=course)

@app.get("/courses/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(database.get_db)):
    course = crud.get_course(db=db, course_id=course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.get("/courses/", response_model=List[schemas.Course])
def read_courses(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_courses(db=db, skip=skip, limit=limit)

@app.post("/students/{student_id}/enroll/", response_model=schemas.EnrolledCourse)
def enroll_student(student_id: int, course: schemas.EnrolledCourseCreate, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db=db, student_id=student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db_course = crud.get_course(db=db, course_id=course.course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return crud.enroll_student_in_course(db=db, student_id=student_id, course_id=course.course_id)

@app.get("/students/{student_id}/courses/", response_model=List[schemas.Course])
def get_student_courses(student_id: int, db: Session = Depends(database.get_db)):
    return crud.get_student_courses(db=db, student_id=student_id)
