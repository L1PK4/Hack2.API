from app.models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Faculty(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    university_id = Column(Integer, ForeignKey(
        'university.id', ondelete='CASCADE'), index=True, nullable=False)

    university = relationship(
        'University',
        back_populates='faculties'
    )
    fields = relationship(
        'Field',
        back_populates='faculty'
    )
