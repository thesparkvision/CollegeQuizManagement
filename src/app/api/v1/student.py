from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.schemas.student import StudentsSchema, StudentSchema, Student, UpdateStudent
from app.config.postgres import get_db_session
from app.services import student as student_service
from app.config.logger import logger

router = APIRouter(prefix="/students")

@router.post(
    "",
    description="API to add a new student to database",
    response_model=None,
    status_code=status.HTTP_201_CREATED
)
def add_student(
    student_details: Student,
    db_session: Session = Depends(get_db_session)
) -> None:
    """
        API to create a new student record in the database.
    """

    try:
        student_service.add_student_record(db_session, student_details)
    except Exception as e:
        logger.error(e, exc_info=True)
        content = {"error": {"detail": str(e)}}
        return JSONResponse(
            content=content,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get(
    "/{student_id}",
    description="API to get student by student id",
    response_model=StudentSchema,
    status_code=status.HTTP_200_OK
)
def get_student(
    student_id: int,
    db_session: Session = Depends(get_db_session)
) -> StudentSchema:
    """
        API to get student by student id.
    """

    try:
        student = student_service.get_student_record(db_session, student_id)
        return {"data": student, "error": None}
    except Exception as e:
        logger.error(e, exc_info=True)
        content = {"error": {"detail": str(e)}}
        return JSONResponse(
            content=content,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.get(
    "",
    description="API to get all students",
    response_model=StudentsSchema,
    status_code=status.HTTP_200_OK
)
def get_all_students( 
    db_session: Session = Depends(get_db_session)
) -> StudentsSchema:
    """
        API to get all students
    """

    try:
        students = student_service.get_all_students(db_session)
        return {"data": students, "error": None}
    except Exception as e:
        logger.error(e, exc_info=True)
        content = {"error": {"detail": str(e)}}
        return JSONResponse(
            content=content,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.patch(
    "/{student_id}",
    description="API to update student details",
    response_model=StudentSchema,
    status_code=status.HTTP_200_OK
)
def update_student_details(
    student_id: int, 
    updated_student_details: UpdateStudent,
    db_session: Session = Depends(get_db_session)
) -> StudentSchema:
    """
        API to update student details for a given student ID.
    """
    
    try:
        student_details = student_service.update_student_details(
            db_session, student_id, updated_student_details
        )
        return {"data": student_details, "error": None}
    except Exception as e:
        logger.error(e, exc_info=True)
        content = {"error": {"detail": str(e)}}
        return JSONResponse(
            content=content,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
@router.delete(
    "/{student_id}",
    description="API to delete student record for a given student ID",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(
    student_id: int,
    db_session: Session = Depends(get_db_session)
) -> None:
    """
        API to delete student record for a given student ID.
    """

    try:
        student_service.delete_student_record(db_session, student_id)
    except Exception as e:
        logger.error(e, exc_info=True)
        content = {"error": {"detail": str(e)}}
        return JSONResponse(
            content=content,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )