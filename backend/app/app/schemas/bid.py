from app.schemas.base import BaseSchema
from app.schemas.offer import GettingOffer
from app.schemas.user import GettingUser
from pydantic import Field


class BaseBid(BaseSchema):
    desired_amount: int


class GettingBid(BaseBid):
    id: int
    is_accepted: bool | None
    actual_amount: int | None
    annual_payment: int | None
    percent: int | None
    created: int
    offer: GettingOffer


class GettingBidByBank(GettingBid):
    user: GettingUser


class UpdatingBid(BaseBid):
    desired_amount: int | None


class CreatingBid(BaseBid):
    pass


class BidApproval(BaseSchema):
    actual_amount: int | None
    annual_payment: int | None
    percent: int | None


class BidCallbackBody(BaseSchema):
    is_accepted: bool | None
    approval: BidApproval | None


class BidApprovalResponse(BaseSchema):
    code: int = Field(..., title='Код ответа')
    error: str | None = Field(None, title='Ошибка')
    bid: GettingBidByBank | None = Field(None, title='Заявка')
