from app.schemas.base import BaseSchema
from app.schemas.city import GettingCity


class BaseUniversity(BaseSchema):
    name: str | None
    lat: str | None
    lon: str | None
    url: str | None


class GettingUniversity(BaseUniversity):
    id: int
    photo: str
    city: GettingCity


class UpdatingUniversity(BaseUniversity):
    city_id: int | None


class CreatingUniversity(BaseUniversity):
    city_id: int
