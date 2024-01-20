from fastapi import APIRouter
from .student import router as student_router

v1_router = APIRouter()
v1_router.include_router(student_router, prefix="/students")