from datetime import datetime

from app.models.base_model import BaseModel
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Bid(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    desired_amount = Column(Integer)
    is_accepted = Column(Boolean)
    created = Column(DateTime, default=datetime.utcnow)
    actual_amount = Column(Integer)
    annual_payment = Column(Integer)
    percent = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    offer_id = Column(Integer, ForeignKey("offer.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="bids", foreign_keys=[user_id])

    offer = relationship("Offer", back_populates="bids")
