from app.getters.bank import get_bank
from app.getters.offer import get_offer
from app.getters.universal import transform
from app.getters.user import get_user
from app.models.bid import Bid
from app.schemas.bid import GettingBid, GettingBidByBank
from app.utils.datetime import to_unix_timestamp
from app.utils.logging import lprint


def get_bid(bid: Bid) -> GettingBid:
    return transform(
        bid,
        GettingBid,
        offer=get_offer(bid.offer),
        created=to_unix_timestamp(bid.created)
    )


def get_bid_by_bank(bid: Bid) -> GettingBidByBank:
    lprint(bid.user.first_name)
    return GettingBidByBank(
        **get_bid(bid).dict(),
        user=get_user(bid.user)
    )
