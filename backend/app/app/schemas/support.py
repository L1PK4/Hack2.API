from app.schemas.bank import GettingBank
from app.schemas.base import BaseSchema
from app.schemas.university import GettingUniversity


class BaseSupport(BaseSchema):
    is_test: bool | None
    url: str | None
    title: str | None
    lesson_count: int | None
    task_count: int | None
    description: str | None
    content: str | None


class GettingSupport(BaseSupport):
    id: int
    university: GettingUniversity | None
    bank: GettingBank | None


class UpdatingSupport(BaseSupport):
    university_id: int | None
    bank_id: int | None


class CreatingSupport(BaseSupport):
    university_id: int | None
    bank_id: int | None
