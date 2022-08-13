from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
import app.models.measurements as schemas
from pygination import paginate
from pygination.models import PageModel
from pygination.errors import PaginationError

router = APIRouter()


@router.get("/{id}", response_model=schemas.Measurements)
def read_measurements(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get item by ID.
    """
    measurements = crud.measurements.get(db=db, id=id)
    if not measurements:
        raise HTTPException(status_code=404, detail="measurements not found")
    return measurements


@router.patch("/{id}", response_model=schemas.Measurements)
def update_measurements(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    measurements_in: schemas.MeasurementsUpdate,
) -> Any:
    """
    Update an item.
    """
    measurements = crud.measurements.get(db=db, id=id)
    if not measurements:
        raise HTTPException(status_code=404, detail="measurements not found")
    measurements = crud.measurements.update(db=db, db_obj=measurements, obj_in=measurements_in)
    return measurements


# @router.delete("/{id}", response_model=schemas.Measurements)
# def delete_measurements(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
# ) -> Any:
#     """
#     Delete an item.
#     """
#     measurements = crud.measurements.get(db=db, id=id)
#     if not measurements:
#         raise HTTPException(status_code=404, detail="measurements not found")
#     measurements = crud.measurements.remove(db=db, id=id)
#     return measurements


@router.post("", response_model=schemas.Measurements)
def create_measurements(
    *,
    db: Session = Depends(deps.get_db),
    body: schemas.MeasurementsCreate,
) -> Any:
    """
    Get item by ID.
    """
    measurements = crud.measurements.create(db=db, obj_in=body)
    if not measurements:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="measurements could not be created",
        )
    return measurements


@router.get("", response_model=List[schemas.Measurements])
def read_measurements(
    *,
    db: Session = Depends(deps.get_db),
    page: int = 0,
    size: int = 50,
    # params: schemas.MeasurementsSearchParams = Depends(),
) -> Any:
    """
    Get item by ID.
    """
    measurements_query = crud.measurements.get_multi(db=db)
    print(measurements_query)

    # try:
    #     pygination_page = paginate(measurements_query, page, size)
    # except (PaginationError, AttributeError) as e:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    # measurements_page = PageModel[schemas.Measurements].from_orm(pygination_page)
    return measurements_query
