"""
database connection module
"""

import psycopg2
from contextlib import contextmanager
from typing import Generator
from sqlmodel import Session, create_engine


class Database:
    """
    Database
    """
    def __init__(self, db_url: str) -> None:
        self._conn = psycopg2.connect(db_url)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """
        session for db connection
        """

        # Create a SQLModel engine
        engine = create_engine('postgresql+psycopg2://', creator=lambda: self._conn)

        # Create a session
        with Session(engine) as session:
            try:
                yield session
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()
