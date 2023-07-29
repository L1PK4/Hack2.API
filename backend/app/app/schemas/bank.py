from app.schemas.base import BaseSchema


class BaseBank(BaseSchema):
    name: str | None
    url: str | None


class GettingBank(BaseBank):
    id: int
    icon: str | None


class UpdatingBank(BaseBank):
    pass


class CreatingBank(BaseBank):
    pass
