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
    '/offers/',
    tags=["Клиентское приложение / Предложения"],
    name="Получить всех предложения",
    response_model=schemas.response.ListOfEntityResponse[schemas.offer.GettingOffer],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_offers(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_user)),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_offer.offer.get_page(
        db=db, page=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.offer.get_offer(offer=offer, user=current_user, db=db)
            for offer in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/offers/',
    tags=["Панель Управления / Предложения"],
    name="Получить всех предложения",
    response_model=schemas.response.ListOfEntityResponse[schemas.offer.GettingOffer],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_offers(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_offer.offer.get_page(
        db=db, page=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.offer.get_offer(offer=offer)
            for offer in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/offers/{offer_id}/',
    tags=["Клиентское приложение / Предложения"],
    name="Получить пользователя по идентификатору",
    response_model=schemas.response.SingleEntityResponse[schemas.offer.GettingOffer],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_offer_by_id(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_user)),
        offer_id: int = Path(...)
):
    offer = crud.crud_offer.offer.get(db=db, id=offer_id)
    if offer is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    return schemas.response.SingleEntityResponse(
        data=getters.offer.get_offer(offer=offer, user=current_user, db=db)
    )


@router.post(
    '/cp/offers/',
    tags=["Панель Управления / Предложения"],
    name="создать пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.offer.GettingOffer],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def create_offer(
        data: schemas.offer.CreatingOffer,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
):
    offer = crud.crud_offer.offer.create(db=db, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.offer.get_offer(offer=offer)
    )


@router.put(
    '/cp/offers/{offer_id}/',
    tags=["Панель Управления / Предложения"],
    name="изменить пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.offer.GettingOffer],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def edit_offer(
        data: schemas.offer.UpdatingOffer,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        offer_id: int = Path(...),
):
    offer = crud.crud_offer.offer.get(db=db, id=offer_id)
    if offer is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    offer = crud.crud_offer.offer.update(
        db=db, db_obj=offer, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.offer.get_offer(offer=offer)
    )


@router.delete(
    '/cp/offers/{offer_id}/',
    tags=["Панель Управления / Предложения"],
    name="удалить пользователя",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403, 400])
)
def delete_offer(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        offer_id: int = Path(...),
):
    crud.crud_offer.offer.remove_by_id(db=db, id=offer_id)

    return schemas.response.OkResponse()
