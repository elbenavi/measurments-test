from fastapi import APIRouter

from app.api.api_v1.endpoints import measurements 

api_router = APIRouter()
api_router.include_router(measurements.router, prefix="/measurements", tags=["Measurements"])

