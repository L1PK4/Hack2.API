from app.models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Bank(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    icon = Column(String)
    url = Column(String)
    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'))
    user = relationship("User", back_populates="banks")
    offers = relationship("Offer", back_populates="bank")

    supports = relationship("Support", back_populates="bank",
                            cascade="all, delete-orphan")
