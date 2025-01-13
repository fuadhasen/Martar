import uuid
from sqlmodel import SQLModel, Field
from datetime import datetime


class BaseModel(SQLModel):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now, onupdate=datetime.now)
