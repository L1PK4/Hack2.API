from app.schemas.base import BaseSchema


class BaseField(BaseSchema):
    name: str | None
    url: str | None
    description: str | None
    min_mark: int | None
    price: int | None


class GettingField(BaseField):
    id: int
    is_selected: bool | None


class UpdatingField(BaseField):
    faculty_id: int | None


class CreatingField(BaseField):
    faculty_id: int
