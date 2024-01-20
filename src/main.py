from fastapi import FastAPI
from app.api.healthcheck import router as healthcheck_router
from app.api.v1 import v1_router

app = FastAPI()
app.include_router(healthcheck_router, prefix="/api/health", tags=["healthcheck"])
app.include_router(v1_router, prefix="/api/v1", tags=["service"])