from app.models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Offer(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    min_price = Column(Integer)
    max_price = Column(Integer)
    percent = Column(Integer)
    annual_payment = Column(Integer)
    payment_term = Column(Integer)
    bank_id = Column(Integer, ForeignKey("bank.id", ondelete="CASCADE"))

    bank = relationship("Bank", back_populates="offers")
    bids = relationship("Bid", back_populates="offer")
