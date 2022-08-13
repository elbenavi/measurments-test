from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
import datetime as dt

class MeasurementsBase(SQLModel):
    latitude: float
    longitude: float
    altitude: float


class Measurements(MeasurementsBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: dt.datetime = Field(default_factory=dt.datetime.utcnow, nullable=False)
    updated_at: Optional[dt.datetime] = Field(
        default=None, sa_column_kwargs={"onupdate": dt.datetime.utcnow}, nullable=True
    )


class MeasurementsRead(MeasurementsBase):
    id: int
    created_at: dt.datetime
    updated_at: Optional[dt.datetime] = None


class MeasurementsCreate(MeasurementsBase):
    pass


class MeasurementsUpdate(SQLModel):
    latitude: float
    longitude: float
    altitude: float
