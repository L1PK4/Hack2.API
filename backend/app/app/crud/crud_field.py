from app.crud.base import CRUDBase
from app.models.field import Field
from app.schemas.field import CreatingField, UpdatingField


class CRUDField(CRUDBase[Field, CreatingField, UpdatingField]):
    pass


field = CRUDField(Field)
