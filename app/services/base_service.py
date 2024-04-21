"""
base service for related service functions
"""


class BaseService:
    """
    BaseService
    """
    def __init__(self, repository) -> None:
        self._repository = repository

    def add(self, schema):
        """
        add method
        """
        return self._repository.create(schema)

    def get_by_id(self, id: int):
        """
        get by id
        """
        return self._repository.read_by_id(id)
