from fastapi import APIRouter
from .student import router as student_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(student_router)