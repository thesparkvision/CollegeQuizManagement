from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, func

Base = declarative_base()
metadata = Base.metadata

class BaseClass(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())