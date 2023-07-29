from typing import Any

from app.models.base_model import BaseModel
from app.utils.auth_session.models import AuthSessionMixin
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, AuthSessionMixin):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    patronymic = Column(String, index=True)

    email = Column(String, unique=True, index=True, nullable=True)
    tel = Column(String, unique=True, index=True, nullable=True)
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    last_activity = Column(DateTime, nullable=True)

    birthdate = Column(DateTime, nullable=True)
    avatar = Column(String, nullable=True)
    gender = Column(Integer, nullable=True)
    auth_sessions = relationship(
        'AuthSession', back_populates='user', passive_deletes=True, cascade="all, delete-orphan")

    banks = relationship(
        'Bank', back_populates='user',
        passive_deletes=True, cascade="all, delete-orphan"
    )

    bids = relationship(
        'Bid', back_populates='user', passive_deletes=True, cascade="all, delete-orphan"
    )
    user_fields = relationship(
        'UserField', back_populates='user', passive_deletes=True, cascade="all, delete-orphan"
    )
