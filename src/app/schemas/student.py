from pydantic import BaseModel, model_validator
from typing import List
from datetime import date

from app.schemas.base import ErrorSchema, check_at_least_one_field_provided

class Student(BaseModel):
    name: str
    email: str
    doj: date
    dob: date
    address: str

class ExtendedStudent(Student):
    id: int

class UpdateStudent(BaseModel):
    name: str | None
    doj: date | None
    dob: date | None
    address: str | None

    # @model_validator(mode='after')
    # def check_update_possibility(self):
    #     return check_at_least_one_field_provided(self.values)

class StudentSchema(BaseModel):
    data: ExtendedStudent
    error: ErrorSchema | None

class StudentsSchema(BaseModel):
    data: List[ExtendedStudent]
    error: ErrorSchema | None