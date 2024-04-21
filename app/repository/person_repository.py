"""
person repository
"""

from typing import Callable
from sqlmodel import Session
from app.model.person import Person
from app.repository.base_repository import BaseRepository


class PersonRepository(BaseRepository):
    """
    UserRepository
    """
    def __init__(self, session_factory: Callable[[], Session]):
        super().__init__(session_factory, Person)
