from sqlalchemy.orm import Session
from typing import List

from app.db.models.student import Student
from app.schemas import student as student_schema

def get_student_by_email(
    db_session: Session, 
    email: str
) -> Student | None:
    """
        Get Student Record with the given email id from student table
    """

    return db_session.query(Student).filter(Student.email == email).first()

def get_student_by_ID(
    db_session: Session, 
    id: int
) -> Student | None:
    """"
        Get the student record with given ID from student table.
    """
    
    return db_session.query(Student).filter(Student.id == id).first()

def get_students(
    db_session: Session
) -> List[Student]:
    """
        Get all matching student records from student table.
    """
    
    return db_session.query(Student).all()

def add_student_record(
    db_session: Session, 
    new_student: Student
) -> int:
    """
        Add a student record to student table.
    """
    
    db_session.add(new_student)
    db_session.commit()
    return new_student.id

def delete_student_record(
    db_session: Session, 
    student_to_delete: Student
) -> None:
    """
        Delete a student record from student table in DB.
    """
    
    db_session.delete(student_to_delete)
    db_session.commit()

def update_student_record(
    db_session: Session, 
    student_record_to_update: Student, 
    updated_student_details: student_schema.Student
) -> Student:
    
    for field, value in updated_student_details.dict().items():
        setattr(student_record_to_update, field, value)

    db_session.commit()

    return student_record_to_update