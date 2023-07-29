from app.getters.field import get_field
from app.getters.universal import transform
from app.models import User
from app.schemas import GettingUser
from app.utils.datetime import to_unix_timestamp


def get_user(user: User) -> GettingUser:
    fields = [
        get_field(user_fields.field)
        for user_fields
        in user.user_fields
    ]
    extra = {
        'fields': fields,
        'birthdate': to_unix_timestamp(user.birthdate),
    }
    if hasattr(user, 'last_activity'):
        extra['last_activity'] = to_unix_timestamp(user.last_activity)

    return transform(db_obj=user, target_schema=GettingUser, **extra)
