import uuid
from sqlmodel import Field
from api.db.models import BaseModel


class Airport(BaseModel):
    name: str
    code: str
    city: str
    country: str


class TransportService(BaseModel):
    name: str
    description: str
    airport_id: uuid.UUID
    vehicle_id: uuid.UUID
