from fastapi import APIRouter
from fastapi import status
from sqlalchemy import text

from app.constants import ServiceStatusEnum
from app.config.logger import logger
from app.config.postgres import SessionLocal
from app.schemas.healthcheck import LiveResponseSchema, ReadyResponseSchema

router = APIRouter()

@router.get(
    "/live",
    description="API to check if the service is live",
    response_model=LiveResponseSchema,
    status_code = status.HTTP_200_OK
)
def check_app_is_live() -> LiveResponseSchema:
    response = {
        "status": ServiceStatusEnum.UP
    }
    return response

@router.get(
    "/ready",
    description="API to check if the service is up and all the required resources can be accessed",
    response_model=ReadyResponseSchema,
    status_code = status.HTTP_200_OK
)
def check_app_health() -> ReadyResponseSchema:
    can_access_db =  is_db_connected()
    status = ServiceStatusEnum.UP if can_access_db else ServiceStatusEnum.DOWN

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