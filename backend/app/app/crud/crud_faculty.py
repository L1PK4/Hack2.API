

from app.crud.base import CRUDBase
from app.models.faculty import Faculty
from app.schemas.faculty import CreatingFaculty, UpdatingFaculty


class CRUDFaculty(CRUDBase[Faculty, CreatingFaculty, UpdatingFaculty]):
    pass


faculty = CRUDFaculty(Faculty)
