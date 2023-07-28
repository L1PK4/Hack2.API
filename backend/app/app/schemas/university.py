from app.schemas.base import BaseSchema
from app.schemas.city import GettingCity


class BaseUniversity(BaseSchema):
    name: str | None


class GettingUniversity(BaseUniversity):
    id: int
    city: GettingCity


class UpdatingUniversity(BaseUniversity):
    city_id: int | None


class CreatingUniversity(BaseUniversity):
    city_id: int
    
