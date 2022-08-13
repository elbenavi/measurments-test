from app.crud.base import CRUDBase
from app.models.measurements import (
    Measurements,
    MeasurementsRead,
    MeasurementsCreate,
    MeasurementsUpdate,
)


class CRUDSpecies(
    CRUDBase[Measurements, MeasurementsRead, MeasurementsCreate, MeasurementsUpdate,]
):
    pass


measurements = CRUDSpecies(Measurements)
