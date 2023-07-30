from app.getters.universal import transform
from app.models.field import Field
from app.models.user import User
from app.models.user_field import UserField
from app.schemas.field import GettingField
from sqlalchemy.orm import Session


def get_field(
    field: Field,
    user: User | None = None,
    db: Session | None = None,
) -> GettingField:
    is_selected = None
    if user is not None and db is not None:
        is_selected = db.query(UserField).filter(
            UserField.field_id == field.id,
            UserField.user_id == user.id,
        ).first() is not None

    return transform(
        field,
        GettingField,
        is_selected=is_selected,
    )
