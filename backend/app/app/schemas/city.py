from app.schemas.base import BaseSchema


class BaseCity(BaseSchema):
    name: str | None


class GettingCity(BaseCity):
    id: int


class UpdatingCity(BaseCity):
    pass


class CreatingCity(BaseCity):
    pass
