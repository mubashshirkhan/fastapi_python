from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    username: str
    phone: int
    age: int
    grade: str
    email: str


class StudentUpdate(BaseModel):
    username: Optional[str] = None
    phone: Optional[int] = None
    age: Optional[int] = None
    grade: Optional[str] = None
    email: Optional[str] = None
