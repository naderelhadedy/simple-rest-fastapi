"""
person related endpoints
"""

from dependency_injector.wiring import Provide
from fastapi import APIRouter, Depends

from app.schema.person_schema import Person
from app.services.person_service import PersonService
from app.core.container import Container


router = APIRouter(prefix="/person", tags=["person"])


@router.get("/{person_id}", response_model=Person)
async def get_person(
    person_id: int,
    service: PersonService = Depends(Provide[Container.person_service]),
):
    """
    get person by id
    """
    data = service.provider().get_by_id(person_id)
    serialized_data = {k: str(v) for k, v in data.dict().items()}

    return Person(**serialized_data)
