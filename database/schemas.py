from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    email: str
    course: str
    address: str
    contactNo: str
    cgpa: float


class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
