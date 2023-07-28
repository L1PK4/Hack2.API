from app.schemas.base import BaseSchema
from app.schemas.university import GettingUniversity


class BaseFaculty(BaseSchema):
    name: str | None


class GettingFaculty(BaseFaculty):
    id: int
    university: GettingUniversity


class UpdatingFaculty(BaseFaculty):
    university_id: int | None


class CreatingFaculty(BaseFaculty):
    university_id: int
