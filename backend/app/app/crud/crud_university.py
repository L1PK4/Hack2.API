

from typing import Type

from app import deps
from app.crud.base import CRUDBase
from app.crud.media import MixinContent
from app.models.university import University
from app.schemas.university import CreatingUniversity, UpdatingUniversity


class CRUDUniversity(CRUDBase[University, CreatingUniversity, UpdatingUniversity], MixinContent):
    def __init__(self, model: type[University]):
        self._storage = deps.get_storage()
        self._content_column = 'photo'
        super().__init__(model)


university = CRUDUniversity(University)
