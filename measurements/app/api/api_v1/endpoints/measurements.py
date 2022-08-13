from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
import requests

import app.models.measurements as schemas
from app.core.config import settings

router = APIRouter()


@router.get("/{id}", response_model=schemas.Measurements)
def read_measurements(id) -> Any:
    url = f'{settings.MEASUREMENTS_HOST}/api/v1/measurements/{id}'
    req = requests.get(url)
    print(req.json())
    return req.json()


@router.get("/")
def read_measurements() -> Any:
    url = f'{settings.MEASUREMENTS_HOST}/api/v1/measurements'
    req = requests.get(url)
    print(req.json())
    return req.json()
