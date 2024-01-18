from fastapi import APIRouter, Depends, status
from sqlalchemy import text

from app.constants import ServiceStatus
from app.config.logger import logger
from app.config.postgres import SessionLocal

router = APIRouter()

@router.get("/ready")
def check_app_health() -> None:
    response = {
        "status": ServiceStatus.UP
    }

    return response

@router.get("/live")
def check_app_health() -> None:
    can_access_db =  is_db_connected()
    status = ServiceStatus.UP if can_access_db else ServiceStatus.DOWN

    response = {
        "status": status,
        "checks": {
            "db": status
        }
    }

    return response

def is_db_connected() -> bool:
    """
    Function to check for database connectivity during app start.
    """
    try:
        db: Session = SessionLocal()
        db.execute(text("SELECT 1"))
        return True
    except Exception as e:
        logger.error(e)
        return False