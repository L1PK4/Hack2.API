from app.schemas.bank import GettingBank
from app.schemas.base import BaseSchema


class BaseOffer(BaseSchema):
    title: str | None
    min_price: int | None
    max_price: int | None
    percent: int | None
    annual_payment: int | None
    payment_term: int | None


class GettingOffer(BaseOffer):
    id: int
    bank: GettingBank


class UpdatingOffer(BaseOffer):
    pass


class CreatingOffer(BaseOffer):
    pass
