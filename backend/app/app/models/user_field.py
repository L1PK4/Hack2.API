from app.models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class UserField(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey(
        'user.id', ondelete='CASCADE'), index=True, nullable=False)
    field_id = Column(Integer, ForeignKey(
        'field.id', ondelete='CASCADE'), index=True, nullable=False)

    user = relationship('User', back_populates='user_fields')
    field = relationship('Field', back_populates='user_fields')
