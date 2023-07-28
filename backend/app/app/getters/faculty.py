from app.getters.universal import transform
from app.getters.university import get_university
from app.models.faculty import Faculty
from app.schemas.faculty import GettingFaculty


def get_faculty(faculty: Faculty) -> GettingFaculty:
    return transform(
        faculty,
        GettingFaculty,
        university=get_university(faculty.university)
    )