from sqlalchemy.orm import Session
import database.models as models
import database.schemas as schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student

def create_academic_history(db: Session, academic: schemas.AcademicHistoryCreate, student_id: int):
    db_academic = models.AcademicHistory(**academic.dict(), student_id=student_id)
    db.add(db_academic)
    db.commit()
    db.refresh(db_academic)
    return db_academic

def get_academic_history(db: Session, student_id: int):
    return db.query(models.AcademicHistory).filter(models.AcademicHistory.student_id == student_id).all()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Course).offset(skip).limit(limit).all()

def enroll_student_in_course(db: Session, student_id: int, course_id: int):
    existing_enrollment = db.query(models.EnrolledCourse).filter_by(
        student_id=student_id, course_id=course_id
    ).first()
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")
    
    db_enrollment = models.EnrolledCourse(student_id=student_id, course_id=course_id)
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment

def get_student_courses(db: Session, student_id: int):
    return db.query(models.Course).join(models.EnrolledCourse).filter(
        models.EnrolledCourse.student_id == student_id
    ).all()
