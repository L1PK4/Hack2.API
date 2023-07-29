from typing import Literal

from app import crud, deps, getters, models, schemas
from app.exceptions import UnfoundEntity
from app.utils.auth_session.deps import in_auth_session
from app.utils.auth_session.schemas import GettingAuthSession
from app.utils.logging import lprint
from app.utils.response import get_responses_description_by_codes
from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    '/banks/',
    tags=["Клиентское приложение / Банки"],
    name="Получить всех банки",
    response_model=schemas.response.ListOfEntityResponse[schemas.bank.GettingBank],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_banks(
        db: Session = Depends(deps.get_db),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_bank.bank.get_page(
        db=db, page=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.bank.get_bank(bank=bank)
            for bank in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/banks/',
    tags=["Панель Управления / Банки"],
    name="Получить всех банки",
    response_model=schemas.response.ListOfEntityResponse[schemas.bank.GettingBank],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_banks(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_bank.bank.get_page(
        db=db, page=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.bank.get_bank(bank=bank)
            for bank in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/banks/{bank_id}/',
    tags=["Панель Управления / Банки"],
    name="Получить пользователя по идентификатору",
    response_model=schemas.response.SingleEntityResponse[schemas.bank.GettingBank],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
@router.get(
    '/banks/{bank_id}/',
    tags=["Клиентское приложение / Банки"],
    name="Получить пользователя по идентификатору",
    response_model=schemas.response.SingleEntityResponse[schemas.bank.GettingBank],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_bank_by_id(
        db: Session = Depends(deps.get_db),
        bank_id: int = Path(...)
):
    bank = crud.crud_bank.bank.get(db=db, id=bank_id)
    if bank is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    return schemas.response.SingleEntityResponse(
        data=getters.bank.get_bank(bank=bank)
    )


@router.post(
    '/cp/banks/',
    tags=["Панель Управления / Банки"],
    name="создать пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.bank.GettingBank],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def create_bank(
        data: schemas.bank.CreatingBank,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
):
    bank = crud.crud_bank.bank.create(db=db, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.bank.get_bank(bank=bank)
    )


@router.put(
    '/cp/banks/{bank_id}/',
    tags=["Панель Управления / Банки"],
    name="изменить пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.bank.GettingBank],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def edit_bank(
        data: schemas.bank.UpdatingBank,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        bank_id: int = Path(...),
):
    bank = crud.crud_bank.bank.get(db=db, id=bank_id)
    if bank is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    bank = crud.crud_bank.bank.update(
        db=db, db_obj=bank, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.bank.get_bank(bank=bank)
    )


@router.delete(
    '/cp/banks/{bank_id}/',
    tags=["Панель Управления / Банки"],
    name="удалить пользователя",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403, 400])
)
def delete_bank(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        bank_id: int = Path(...),
):
    crud.crud_bank.bank.remove_by_id(db=db, id=bank_id)

    return schemas.response.OkResponse()
