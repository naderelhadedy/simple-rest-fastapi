"""
database connection module
"""

import psycopg2
from contextlib import closing, contextmanager
from typing import Generator
from sqlmodel import Session


class Database:
    """
    Database
    """
    def __init__(self, db_url: str) -> None:
        self._conn = psycopg2.connect(db_url)
        # self._conn.autocommit = True

    def session(self):
        return self._conn

    # @contextmanager
    # def session(self) -> Generator[Session, None, None]:
    #     """
    #     session
    #     """
    #     with closing(self._conn.cursor()) as cursor:
    #         session = Session(cursor)
    #         try:
    #             yield session
    #         except Exception as e:
    #             session.rollback()
    #             raise e
    #         finally:
    #             session.close()
