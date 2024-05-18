"""
person service
"""

from app.repository.person_repository import PersonRepository
from app.services.base_service import BaseService


class PersonService(BaseService):
    """
    PersonService
    """
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository
        super().__init__(person_repository)
