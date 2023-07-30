from app.getters.bank import get_bank
from app.getters.universal import transform
from app.models.bid import Bid
from app.models.offer import Offer
from app.models.user import User
from app.schemas.offer import GettingOffer
from sqlalchemy.orm import Session


def get_offer(offer: Offer, user: User | None = None, db: Session | None = None) -> GettingOffer:
    is_sent = None
    if user is not None and db is not None:
        is_sent = db.query(Bid).filter(
            Bid.user_id == user.id,
            Bid.offer_id == offer.id
        ).first() is not None
    return transform(
        offer,
        GettingOffer,
        is_sent=is_sent,
        bank=get_bank(offer.bank) if offer.bank is not None else None
    )
