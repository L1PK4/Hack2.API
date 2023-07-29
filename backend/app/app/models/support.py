from app.models.base_model import BaseModel
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Support(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    bank_id = Column(Integer, ForeignKey(
        "bank.id", ondelete='CASCADE'), index=True)

    bank = relationship(
        "Bank", back_populates="supports"
    )

    university_id = Column(Integer, ForeignKey(
        "university.id", ondelete='CASCADE'), index=True)

    university = relationship(
        "University",
        back_populates="supports"
    )

    is_test = Column(Boolean, default=False)
    url = Column(String)
    title = Column(String)
    lesson_count = Column(Integer)
    task_count = Column(Integer)
    description = Column(String)
    content = Column(String)
