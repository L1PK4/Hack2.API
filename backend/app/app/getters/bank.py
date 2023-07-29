from app.getters.universal import transform
from app.models.bank import Bank
from app.schemas.bank import GettingBank


def get_bank(bank: Bank) -> GettingBank:
    return transform(
        bank,
        GettingBank
    )
