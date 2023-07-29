from app.getters.bank import get_bank
from app.getters.universal import transform
from app.getters.user import get_user
from app.models.bid import Bid
from app.schemas.bid import GettingBid, GettingBidByBank
from app.utils.datetime import to_unix_timestamp


def get_bid(bid: Bid) -> GettingBid:
    return transform(
        bid,
        GettingBid,
        bank=get_bank(bid.bank),
        created=to_unix_timestamp(bid.created)
    )


def get_bid_by_bank(bid: Bid) -> GettingBidByBank:
    return GettingBidByBank(
        **get_bid(bid).dict(),
        user=get_user(bid.user)
    )
