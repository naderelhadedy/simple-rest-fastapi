"""
base repository for related database functions
"""

from typing import Callable
from sqlmodel import Session
import psycopg2

from app.core.exceptions import DuplicatedError, NotFoundError


class BaseRepository:
    """
    BaseRepository
    """
    def __init__(self, session_factory, model) -> None:
        self.session_factory = session_factory
        self.model = model
    # def __init__(self, session_factory: Callable[[], Session], model) -> None:
    #     self.session_factory = session_factory
    #     self.model = model

    def create(self, schema):
        """
        create method
        """
        with self.session_factory() as session:
            query = self.model(**schema.dict())
            try:
                session.add(query)
                session.commit()
            except psycopg2.IntegrityError as e:
                raise DuplicatedError(detail=str(e))
            return query

    def read_by_id(self, id: int):
        """
        read by id method
        """
        with self.session_factory() as session:
            return session.cursor().execute(f"SELECT * FROM persons WHERE id={id};")
        # with self.session_factory() as session:
        #     query = session.get(self.model, id)
        #     if query is None:
        #         raise NotFoundError(detail=f"not found id : {id}")
        #     return query