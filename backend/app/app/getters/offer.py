from app.getters.bank import get_bank
from app.getters.universal import transform
from app.models.offer import Offer
from app.schemas.offer import GettingOffer


def get_offer(offer: Offer) -> GettingOffer:
    return transform(
        offer,
        GettingOffer,
        bank=get_bank(offer.bank)
    )
