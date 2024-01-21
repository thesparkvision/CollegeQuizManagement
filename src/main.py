from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.cors import CORSMiddleware

from app.api.healthcheck import router as healthcheck_router
from app.api.v1 import v1_router
from app.config.settings import app_settings

allowed_origins = app_settings.allowed_origins.split(",")

app = FastAPI(root_path="/api")
app.add_middleware(HTTPSRedirectMiddleware)
if allowed_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(healthcheck_router, tags=["healthcheck"])
app.include_router(v1_router, tags=["service"])