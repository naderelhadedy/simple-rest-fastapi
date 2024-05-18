"""
container module
"""

from dependency_injector import containers, providers

from app.core.config import Configs
from app.core.database import Database
from app.repository import *
from app.services import *


class Container(containers.DeclarativeContainer):
    """
    Container class
    """
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.person",
        ]
    )

    db = providers.Singleton(Database, db_url=Configs.DATABASE_URI)

    person_repository = providers.Factory(PersonRepository, session_factory=db.provided.session)

    person_service = providers.Factory(PersonService, person_repository=person_repository)
