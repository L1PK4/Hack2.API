from app.models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class University(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    lat = Column(String)
    lon = Column(String)
    address = Column(String)
    photo = Column(String)
    url = Column(String)
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

    supports = relationship(
        'Support',
        back_populates='university',
        cascade='all, delete-orphan'
    )
