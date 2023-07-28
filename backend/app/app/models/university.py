from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String
from app.models.base_model import BaseModel


class University(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    city_id = Column(
        Integer,
        ForeignKey('city.id', ondelete='CASCADE'),
        index=True,
        nullable=False
        )

    city = relationship(
        'City',
        back_populates='universities'
        )
    faculties = relationship(
        'Faculty',
        back_populates='university'
    )