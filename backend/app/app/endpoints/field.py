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
    '/fields/',
    tags=["Клиентское приложение / Направления"],
    name="Получить всех направления",
    response_model=schemas.response.ListOfEntityResponse[schemas.field.GettingField],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_fields(
        db: Session = Depends(deps.get_db),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_field.field.get_page(
        db=db, pag=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.field.get_field(field=field)
            for field in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/fields/',
    tags=["Панель Управления / Направления"],
    name="Получить всех направления",
    response_model=schemas.response.ListOfEntityResponse[schemas.field.GettingField],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_fields(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_field.field.get_page(
        db=db, pag=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.field.get_field(field=field)
            for field in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/fields/{field_id}/',
    tags=["Панель Управления / Направления"],
    name="Получить пользователя по идентификатору",
    response_model=schemas.response.SingleEntityResponse[schemas.field.GettingField],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_field_by_id(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        field_id: int = Path(...)
):
    field = crud.crud_field.field.get(db=db, id=field_id)
    if field is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    return schemas.response.SingleEntityResponse(
        data=getters.field.get_field(field=field)
    )


@router.post(
    '/cp/fields/',
    tags=["Панель Управления / Направления"],
    name="создать пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.field.GettingField],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def create_field(
        data: schemas.field.CreatingField,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
):
    field = crud.crud_field.field.create(db=db, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.field.get_field(field=field)
    )


@router.put(
    '/cp/fields/{field_id}/',
    tags=["Панель Управления / Направления"],
    name="изменить пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.field.GettingField],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def edit_field(
        data: schemas.field.UpdatingField,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        field_id: int = Path(...),
):
    field = crud.crud_field.field.get(db=db, id=field_id)
    if field is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    field = crud.crud_field.field.update(
        db=db, db_obj=field, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.field.get_field(field=field)
    )


@router.delete(
    '/cp/fields/{field_id}/',
    tags=["Панель Управления / Направления"],
    name="удалить пользователя",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403, 400])
)
def delete_field(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        field_id: int = Path(...),
):
    crud.crud_field.field.remove_by_id(db=db, id=field_id)

    return schemas.response.OkResponse()
