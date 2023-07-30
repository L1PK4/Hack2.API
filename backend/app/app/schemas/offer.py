from app.schemas.bank import GettingBank
from app.schemas.base import BaseSchema
from pydantic import Field


class BaseOffer(BaseSchema):
    title: str | None
    min_price: int | None
    max_price: int | None
    percent: int | None
    annual_payment: int | None
    payment_term: int | None


class GettingOffer(BaseOffer):
    id: int
    is_sent: bool | None = Field(None)
    bank: GettingBank


class UpdatingOffer(BaseOffer):
    bank_id: int | None


class CreatingOffer(BaseOffer):
    bank_id: int
