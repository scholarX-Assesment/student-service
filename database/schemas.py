from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import datetime


class AcademicHistoryBase(BaseModel):
    year: int
    achievement: str

    @validator('year')
    def validate_year(cls, year):
        current_year = datetime.now().year
        if year > current_year:
            raise ValueError("Year cannot be in the future")
        return year


class AcademicHistoryCreate(AcademicHistoryBase):
    pass


class AcademicHistory(AcademicHistoryBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True


class EnrolledCourseBase(BaseModel):
    course_id: int


class EnrolledCourseCreate(EnrolledCourseBase):
    pass


class EnrolledCourse(EnrolledCourseBase):
    id: int
    student_id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    name: str
    email: str
    address: str
    contactNo: str
    cgpa: float


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    academic_history: List[AcademicHistory] = []
    enrolled_courses: List[EnrolledCourse] = []

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None
    credits: float


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True
