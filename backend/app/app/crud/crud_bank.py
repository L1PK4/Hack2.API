from app import deps
from app.crud.base import CRUDBase
from app.crud.media import MixinContent
from app.models.bank import Bank
from app.schemas.bank import CreatingBank, UpdatingBank


class CRUDBank(CRUDBase[Bank, CreatingBank, UpdatingBank], MixinContent):
    def __init__(self, model: type[Bank]):
        self._storage = deps.get_storage()
        self._content_column = 'icon'
        super().__init__(model)


bank = CRUDBank(Bank)
