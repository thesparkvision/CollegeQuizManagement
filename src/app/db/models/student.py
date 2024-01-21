from sqlalchemy import Column, Column, String, Date, Integer, DateTime, func

from app.db.models.base import Base

class BaseClass(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Student(BaseClass):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    doj = Column(Date, nullable=False)
    dob = Column(Date, nullable=False)
    address = Column(String(200), nullable=True)