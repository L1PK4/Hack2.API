from app.crud.base import CRUDBase
from app.models.field import Field
from app.models.user import User
from app.models.user_field import UserField
from app.schemas.field import CreatingField, UpdatingField
from sqlalchemy.orm import Session


class CRUDField(CRUDBase[Field, CreatingField, UpdatingField]):
    def add_field(self, db: Session, *, field: Field, user: User) -> Field:
        db_obj = UserField()
        db_obj.field = field
        db_obj.user = user
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj.field


field = CRUDField(Field)
