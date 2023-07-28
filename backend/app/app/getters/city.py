
from app.getters.universal import transform
from app.models.city import City
from app.schemas.city import GettingCity


def get_city(city: City) -> GettingCity:
    return transform(
        city,
        GettingCity
    )