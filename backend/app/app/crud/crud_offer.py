from app.crud.base import CRUDBase
from app.models.offer import Offer
from app.schemas.offer import CreatingOffer, UpdatingOffer


class CRUDOffer(CRUDBase[Offer, CreatingOffer, UpdatingOffer]):
    pass


offer = CRUDOffer(Offer)
