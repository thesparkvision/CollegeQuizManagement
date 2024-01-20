from fastapi import APIRouter, status
from app.schemas.student import StudentsSchema, StudentSchema, Student, UpdateStudent
from app.schemas.base import ErrorSchema

router = APIRouter()

@router.post(
    "",
    description="API to add a new student to database",
    response_model=StudentSchema,
    status_code=status.HTTP_200_OK
)
def add_student(student: Student) -> StudentSchema:
    """
        API to create a new student record in the database.
    """

    return {"data": None, "error": None}


@router.get(
    "/{student_id}",
    description="API to get student by student id",
    response_model=StudentSchema,
    status_code=status.HTTP_200_OK
)
def get_student(student_id: int) -> StudentSchema:
    """
        API to get student by student id.
    """
    
    return {"data": None, "error": None}

@router.get(
    "",
    description="API to get all students",
    response_model=StudentsSchema,
    status_code=status.HTTP_200_OK
)
def get_all_students() -> StudentsSchema:
    """
        API to get all students
    """

    return {"data": [], "error": None}

@router.patch(
    "/{student_id}",
    description="API to update student details",
    response_model=StudentSchema,
    status_code=status.HTTP_200_OK
)
def update_student_details(student_id: int, student: UpdateStudent) -> StudentSchema:
    """
        API to update student details for a given student ID.
    """

    return {"data": None, "error": None}

@router.delete(
    "/{student_id}",
    description="API to delete student record for a given student ID",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int) -> None:
    """
        API to delete student record for a given student ID.
    """
    pass