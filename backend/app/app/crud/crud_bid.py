from typing import Any

from app.crud.base import CRUDBase
from app.enums.bid import BidStatus
from app.exceptions import UnprocessableEntity
from app.models.bank import Bank
from app.models.bid import Bid
from app.models.offer import Offer
from app.models.user import User
from app.schemas.bid import BidApproval, CreatingBid, UpdatingBid
from sqlalchemy.orm import Query, Session


class CRUDBid(CRUDBase[Bid, CreatingBid, UpdatingBid]):
    def accept(
            self,
            db: Session,
            *,
            bid: Bid,
            bank: Bank,
            approval: BidApproval,
            verification_sert: str
    ) -> Bid:
        approved = self._check_bank(
            db, bank=bank, verification_sert=verification_sert
        )
        if not approved:
            raise UnprocessableEntity("Не удалось подтвердить банк")
        bid.actual_amount = approval.actual_amount
        bid.annual_payment = approval.annual_payment
        bid.percent = approval.percent
        bid.is_accepted = True
        db.add(bid)
        db.commit()
        db.refresh(bid)
        return bid

    def _check_bank(
            self,
            db: Session,
            *,
            bank: Bank,
            verification_sert: str
    ) -> bool:
        return True

    def decline(
            self,
            db: Session,
            *,
            bank: Bank,
            bid: Bid,
            verification_sert: str
    ) -> Bid:
        approved = self._check_bank(
            db, bank=bank, verification_sert=verification_sert
        )
        if not approved:
            raise UnprocessableEntity("Не удалось подтвердить банк")

        bid.is_accepted = False
        db.add(bid)
        db.commit()
        db.refresh(bid)
        return bid

    def _get_filter_by_name(self, name):

        match name:
            case 'banks':
                def filter(query: Query, value: Any) -> Query:
                    ids = [bank.id for bank in value]
                    query = query.join(Offer)
                    return query.filter(Offer.bank_id.in_(ids))
                return filter
            case 'bid_status':
                def filter(query: Query, value: BidStatus) -> Query:
                    if value == "pending":
                        return query.filter(Bid.is_accepted.is_(None))
                    elif value == "accepted":
                        return query.filter(Bid.is_accepted.is_(True))
                    elif value == "declined":
                        return query.filter(Bid.is_accepted.is_(False))
                return filter
            case _:
                return None


bid = CRUDBid(Bid)
