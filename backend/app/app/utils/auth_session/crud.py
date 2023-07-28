from app.crud.base import CRUDBase
from app.models import AuthSession
from app.schemas import CreatingAuthSession, UpdatingAuthSession


class CRUDAuthSession(CRUDBase[AuthSession, CreatingAuthSession, UpdatingAuthSession]):
    def _get_filter_by_name(self, name):
        match name:
            case "is_ended":
                return lambda query, value: query.filter((self.model.ended != None) == value)


auth_session = CRUDAuthSession(AuthSession)
