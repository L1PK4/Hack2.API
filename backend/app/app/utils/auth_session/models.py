import datetime
from typing import Any

from app.models.base_model import BaseModel
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class AuthSession(BaseModel):
    id = Column(Integer, primary_key=True, index=True)

    created = Column(DateTime, nullable=False,
                     default=datetime.datetime.utcnow)
    ended = Column(DateTime, nullable=True, default=None)
    last_activity = Column(DateTime, nullable=False,
                           default=datetime.datetime.utcnow)

    ip_address = Column(String, nullable=True)
    accept_language = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    detected_os = Column(String, nullable=True)
    firebase_token = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)

    user = relationship('User', back_populates='auth_sessions')


class AuthSessionMixin:
    jwt_payload: dict[str | Any] | None = None
    auth_session: AuthSession | None = None
