from fastapi import FastAPI
from pydantic import BaseModel


class Measurements(BaseModel):
    latitude: float
    longitude: float
    altitude: float