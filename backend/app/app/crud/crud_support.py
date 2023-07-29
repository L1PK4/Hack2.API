from app.crud.base import CRUDBase
from app.enums.support import SupportType
from app.models.support import Support
from app.schemas.support import CreatingSupport, UpdatingSupport
from sqlalchemy.orm import Query


class CRUDSupport(CRUDBase[Support, CreatingSupport, UpdatingSupport]):
    def _get_filter_by_name(self, name):
        match name:
            case "support_type":
                def filter(query: Query, value: SupportType) -> Query:
                    if value == "financial":
                        return query.filter(Support.bank_id.is_not(None))
                    if value == "university":
                        return query.filter(Support.university_id.is_not(None))
                    if value == "else":
                        return query.filter(
                            Support.bank_id.is_(None),
                            Support.university_id.is_(None),
                        )
                return filter
            case _:
                return None


support = CRUDSupport(Support)
