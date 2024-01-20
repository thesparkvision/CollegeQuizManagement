from pydantic import BaseModel
from typing import Dict

from app.constants import ServiceStatusEnum, ServicesEnum

class LiveResponseSchema(BaseModel):
    status: ServiceStatusEnum

class ReadyResponseSchema(BaseModel):
    status: ServiceStatusEnum
    checks: Dict[ServicesEnum, ServiceStatusEnum]