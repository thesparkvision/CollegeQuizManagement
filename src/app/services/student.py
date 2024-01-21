from sqlalchemy.orm import Session

from app.schemas import student as student_schema
from app.db.models.student import Student
from app.db.postgres import student as student_table

def add_student_record(
    db_session: Session, 
    student_details: student_schema.Student
) -> None:
    """
        Service method to add new user to system.
        If user exist, then it raises error.
    """
    
    student_email = student_details.email
    existing_student: Student = student_table.get_student_by_email(db_session, student_email)
    if existing_student:
        raise Exception("Student already exist with this email id!")
    
    new_student = Student(**student_details.dict())

    new_student_id = student_table.add_student_record(db_session, new_student)
    if not new_student_id:
        raise Exception("Something went wrong with student creation!")

def get_student_record(
    db_session: Session, 
    student_id: int
) -> Student | None:
    """
        Service method to get a student record matching with a student id.
        If student record is not found, it raises error.
    """
    
    student_record = student_table.get_student_by_ID(db_session, student_id)
    if not student_record:
        raise Exception("Student Record with provided ID Not Found!")
    return student_record

def get_all_students(
    db_session: Session
) -> list[Student]:
    """
        Service method to get all students from student table, else return an empty list.
    """
    
    students = student_table.get_students(db_session)
    return students

def update_student_details(
    db_session: Session, 
    student_id: int, 
    updated_student_details: student_schema.UpdateStudent
) -> Student:
    """
        Service method to update student details for a given student.
        If the student with the given student ID does not exist, it raises error.
    """
    
    existing_student: Student = student_table.get_student_by_ID(db_session, student_id)
    if not existing_student:
        raise Exception("Student with the provided ID does not exist!")

    updated_student: Student = student_table.update_student_record(db_session, existing_student, updated_student_details)
    return updated_student

def delete_student_record(
    db_session: Session,
    student_id: int
) -> None:
    """
        Service method to delete a student record if it exist in system, else raise Error.
    """
    
    existing_student: Student = student_table.get_student_by_ID(db_session, student_id)
    if not existing_student:
        raise Exception("Student with the provided ID does not exist!")
    
    student_table.delete_student_record(db_session, existing_student)