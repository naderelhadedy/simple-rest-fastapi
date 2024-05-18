"""
person schema
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Person(BaseModel):
    """
    Person schema
    """
    id: int
    cognito_id: str
    first_name: str
    last_name: str
    birthdate: Optional[str]
    email: str
    phone_number: str
    system_role: str
    consents: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime
