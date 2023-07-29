from typing import Literal

from app import crud, deps, getters, models, schemas
from app.enums.support import SupportType
from app.exceptions import UnfoundEntity
from app.utils.auth_session.deps import in_auth_session
from app.utils.auth_session.schemas import GettingAuthSession
from app.utils.logging import lprint
from app.utils.response import get_responses_description_by_codes
from fastapi import APIRouter, Depends, Path, Query
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    '/supports/',
    tags=["Клиентское приложение / Помощь"],
    name="Получить всех помощь",
    response_model=schemas.response.ListOfEntityResponse[schemas.support.GettingSupport],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_supports(
        db: Session = Depends(deps.get_db),
        is_test: bool | None = Query(None),
        support_type: SupportType | None = Query(None),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_support.support.get_page(
        db=db, page=page, is_test=is_test, support_type=support_type)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.support.get_support(support=support)
            for support in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/supports/',
    tags=["Панель Управления / Помощь"],
    name="Получить всех помощь",
    response_model=schemas.response.ListOfEntityResponse[schemas.support.GettingSupport],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_supports(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_support.support.get_page(
        db=db, page=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.support.get_support(support=support)
            for support in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/supports/{support_id}/',
    tags=["Клиентское приложение / Помощь"],
    name="Получить пользователя по идентификатору",
    response_model=schemas.response.SingleEntityResponse[schemas.support.GettingSupport],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_support_by_id(
        db: Session = Depends(deps.get_db),
        support_id: int = Path(...)
):
    support = crud.crud_support.support.get(db=db, id=support_id)
    if support is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    return schemas.response.SingleEntityResponse(
        data=getters.support.get_support(support=support)
    )


@router.post(
    '/cp/supports/',
    tags=["Панель Управления / Помощь"],
    name="создать пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.support.GettingSupport],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def create_support(
        data: schemas.support.CreatingSupport,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
):
    support = crud.crud_support.support.create(db=db, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.support.get_support(support=support)
    )


@router.put(
    '/cp/supports/{support_id}/',
    tags=["Панель Управления / Помощь"],
    name="изменить пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.support.GettingSupport],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def edit_support(
        data: schemas.support.UpdatingSupport,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        support_id: int = Path(...),
):
    support = crud.crud_support.support.get(db=db, id=support_id)
    if support is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    support = crud.crud_support.support.update(
        db=db, db_obj=support, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.support.get_support(support=support)
    )


@router.delete(
    '/cp/supports/{support_id}/',
    tags=["Панель Управления / Помощь"],
    name="удалить пользователя",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403, 400])
)
def delete_support(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        support_id: int = Path(...),
):
    crud.crud_support.support.remove_by_id(db=db, id=support_id)

    return schemas.response.OkResponse()
