from app.getters.bank import get_bank
from app.getters.universal import transform
from app.getters.university import get_university
from app.models.support import Support
from app.schemas.support import GettingSupport


def get_support(support: Support) -> GettingSupport:
    return transform(
        support,
        GettingSupport,
        bank=get_bank(support.bank) if support.bank is not None else None,
        university=get_university(
            support.university) if support.university is not None else None,
    )
