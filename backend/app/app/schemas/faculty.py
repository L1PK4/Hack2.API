from app.schemas.base import BaseSchema
from app.schemas.field import GettingField
from app.schemas.university import GettingUniversity


class BaseFaculty(BaseSchema):
    name: str | None


class GettingFaculty(BaseFaculty):
    id: int
    university: GettingUniversity
    avg_mark: float = 0.
    fields: list[GettingField]
    min_price: float = 0.


class UpdatingFaculty(BaseFaculty):
    university_id: int | None


class CreatingFaculty(BaseFaculty):
    university_id: int
