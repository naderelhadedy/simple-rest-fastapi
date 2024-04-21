"""
person model
"""

from typing import Optional
from sqlmodel import Field
from pydantic import constr, field_validator

from app.model.base_model import BaseModel


class Person(BaseModel, table=True):
    """
    Person Model
    """
    cognito_id: str = Field(max_length=50)
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    birthdate: Optional[str] = Field(nullable=True)
    email: str = Field(max_length=100)
    phone_number: str = Field(max_length=20)
    system_role: str = constr(max_length=10)
    consents: Optional[str] = Field(nullable=True)
    is_active: bool = Field(default=True)

    @field_validator("system_role")
    def system_role_validation(cls, v):
        if v not in ["Admin", "User"]:
            raise ValueError("System role must be either 'Admin' or 'User'")
        return v
