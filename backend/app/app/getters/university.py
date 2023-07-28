from app.getters.city import get_city
from app.getters.universal import transform
from app.models.university import University
from app.schemas.university import GettingUniversity


def get_university(university: University) -> GettingUniversity:
    return transform(
        university,
        GettingUniversity,
        city=get_city(university.city)
    )