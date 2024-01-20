from sqlalchemy import Column, Column, String, Date, Integer

from models.base import BaseClass

class Student(BaseClass):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    doj = Column(Date, nullable=False)
    dob = Column(Date, nullable=False)
    address = Column(String(200), nullable=True)