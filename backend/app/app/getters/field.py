from app.getters.universal import transform
from app.models.field import Field
from app.schemas.field import GettingField


def get_field(field: Field) -> GettingField:
    return transform(
        field,
        GettingField
    )
