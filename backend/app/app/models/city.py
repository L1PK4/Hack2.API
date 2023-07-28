from sqlalchemy import Column, Integer, String
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship

class City(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    universities = relationship(
        'University',
        back_populates='city'
    )