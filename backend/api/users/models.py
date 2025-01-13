import uuid
import enum
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime

from api.db.models import BaseModel


class RoleEnum(str, enum.Enum):
    tourist = "tourist"
    driver = "driver"
    admin = "admin"
    staff = "staff"


class User(BaseModel):
    name: str
    email: str = Field(index=True, unique=True)
    phone: Optional[str] = Field(default=None)
    password: str
    role: RoleEnum = Field(default=RoleEnum.tourist)
    is_active: bool = Field(default=True)
