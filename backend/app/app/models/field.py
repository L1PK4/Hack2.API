from app.models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Field(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    url = Column(String)
    description = Column(String)
    min_mark = Column(Integer, index=True)
    price = Column(Integer)
    faculty_id = Column(Integer, ForeignKey(
        "faculty.id", ondelete='CASCADE'), index=True)

    faculty = relationship("Faculty", back_populates="fields")
    user_fields = relationship(
        "UserField", back_populates="field", cascade="all, delete-orphan")
