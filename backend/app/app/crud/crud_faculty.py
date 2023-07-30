
from app import deps
from app.crud.base import CRUDBase
from app.models.faculty import Faculty
from app.models.field import Field
from app.models.university import University
from app.schemas.faculty import CreatingFaculty, UpdatingFaculty
from app.session import SessionLocal
from app.utils.datetime import from_unix_timestamp
from app.utils.logging import lprint
from sqlalchemy import alias, cast, func, text
from sqlalchemy.orm import Query


class CRUDFaculty(CRUDBase[Faculty, CreatingFaculty, UpdatingFaculty]):

    def _get_min_cost(
            self,
            query: Query,
            cost_from: int | None = None,
            cost_to: int | None = None,
    ) -> Query:
        db = SessionLocal()
        min_ = func.min(Field.price)

        q1 = db.query(Field.faculty_id, min_).group_by(
            Field.faculty_id).subquery(name=f'min_cost1')
        q = query.join(q1, Faculty.id == q1.c.faculty_id)
        if cost_from is not None:
            q = q.filter(
                text(
                    f" min_cost1.min_1 >= {cost_from}"),
            )
        if cost_to is not None:
            q = q.filter(
                text(
                    f" min_cost1.min_1 <= {cost_to}"),
            )
        lprint(q.statement.compile())
        return q

    def _get_filter_by_name(self, name):
        match name:
            case 'cost_range':
                def filter(query, value):
                    value_from, value_to = value
                    return self._get_min_cost(query, cost_from=value_from, cost_to=value_to)
                return filter
            case 'city_id':
                return lambda query, value: query.join(University).filter(
                    University.city_id == value
                )


faculty = CRUDFaculty(Faculty)
