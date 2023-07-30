from app.getters.field import get_field
from app.getters.universal import transform
from app.getters.university import get_university
from app.models.faculty import Faculty
from app.models.user import User
from app.schemas.faculty import GettingFaculty
from sqlalchemy.orm import Session


def get_faculty(
    faculty: Faculty,
    user: User | None = None,
    db: Session | None = None,
) -> GettingFaculty:
    marks = [
        field.min_mark for field in faculty.fields if field.min_mark is not None
    ]
    prices = [
        field.price for field in faculty.fields if field.price is not None
    ]
    return transform(
        faculty,
        GettingFaculty,
        university=get_university(faculty.university),
        avg_mark=sum(marks) / len(marks) if marks else 0.,
        min_price=min(prices) if prices else 0.,
        fields=[get_field(field, user, db) for field in faculty.fields]
    )
