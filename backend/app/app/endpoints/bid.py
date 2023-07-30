
from app import crud, deps, getters, models, schemas
from app.enums.bid import BidStatus
from app.exceptions import InaccessibleEntity, UnfoundEntity
from app.schemas.response import Meta
from app.utils.auth_session.deps import in_auth_session
from app.utils.logging import lprint
from app.utils.response import get_responses_description_by_codes
from fastapi import APIRouter, Depends, Header, Path, Query
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    "/offers/bids/",
    response_model=schemas.response.ListOfEntityResponse[schemas.GettingBid],
    tags=["Клиентское приложение / Заявки"],
    name="Получить список заявок",
    responses=get_responses_description_by_codes([400, 401, 403])
)
def get_bids(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(
        in_auth_session(deps.get_current_active_user)),
    page: int | None = Query(None)
):
    data, paginator = crud.bid.get_page(
        db=db,
        page=page,
        user_id=current_user.id
    )

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.bid.get_bid(datum)
            for datum
            in data
        ],
        meta=Meta(paginator=paginator)
    )


@router.get(
    "/offers/bids/{bid_id}/",
    response_model=schemas.response.SingleEntityResponse[schemas.GettingBid],
    tags=["Клиентское приложение / Заявки"],
    name="Получить список заявок",
    responses=get_responses_description_by_codes([404, 400, 401, 403])
)
def get_bids(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(
        in_auth_session(deps.get_current_active_user)),
    bid_id: int = Path(...),
):
    data = crud.bid.get(
        db=db,
        id=bid_id
    )
    if data is None:
        raise UnfoundEntity("Заявка не найдена")

    if data.user_id != current_user.id:
        raise InaccessibleEntity("Заявка недоступна")

    return schemas.response.SingleEntityResponse(
        data=getters.get_bid(data),
    )


@router.post(
    '/offers/{offer_id}/bids/',
    name="Создать заявку",
    tags=["Клиентское приложение / Заявки"],
    responses=get_responses_description_by_codes([400, 401, 403, 404]),
    response_model=schemas.response.SingleEntityResponse[schemas.GettingBid]
)
def create_bid(
    data: schemas.CreatingBid,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(
        in_auth_session(deps.get_current_active_user)),
    offer_id: int = Path(...),
):
    bid = crud.bid.create(
        db=db,
        obj_in=data,
        user_id=current_user.id,
        offer_id=offer_id,
    )

    return schemas.response.SingleEntityResponse(
        data=getters.get_bid(bid)
    )


@router.post(
    '/cp/bids/{bid_id}/process/',
    name="Подтвердить / отклонить заявку",
    tags=["Панель управления Банка / Заявки"],
    responses=get_responses_description_by_codes([400, 401, 403, 422]),
    response_model=schemas.response.SingleEntityResponse[schemas.bid.BidApprovalResponse]
)
def approve_bid(
    data: schemas.bid.BidCallbackBody,
    db: Session = Depends(deps.get_db),
    verification_sert: str = Header(..., alias='verification-sert'),
    current_user: models.User = Depends(
        in_auth_session(deps.get_current_active_superuser)),
    bid_id: int = Path(...),
):
    bid = crud.bid.get(
        db=db,
        id=bid_id
    )
    if bid.offer.bank.user_id != current_user.id:
        raise InaccessibleEntity("Заявка недоступна")
    if bid is None:
        raise UnfoundEntity("Заявка не найдена")

    lprint(data.is_accepted)
    if not data.is_accepted:
        bid = crud.bid.decline(
            db=db,
            bank=bid.offer.bank,
            bid=bid,
            verification_sert=verification_sert
        )
    else:
        bid = crud.bid.accept(
            db=db,
            bank=bid.offer.bank,
            bid=bid,
            approval=data.approval,
            verification_sert=verification_sert
        )

    return schemas.response.SingleEntityResponse(
        data=schemas.bid.BidApprovalResponse(
            code=0,
            error=None,
            bid=getters.get_bid_by_bank(bid)
        )
    )


@router.get(
    '/cp/bids/',
    response_model=schemas.response.ListOfEntityResponse[schemas.bid.GettingBidByBank],
    tags=["Панель управления Банка / Заявки"],
    name="Получить список заявок",
    responses=get_responses_description_by_codes([400, 401, 403])
)
def get_bids_by_bank(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(
        in_auth_session(deps.get_current_active_superuser)),
    bid_status: BidStatus | None = Query(None),
    page: int | None = Query(None),
):
    data, paginator = crud.bid.get_page(
        db=db,
        page=page,
        banks=current_user.banks,
        bid_status=bid_status,
        order_by=models.Bid.created.desc()
    )
    return schemas.response.ListOfEntityResponse(
        data=[
            getters.bid.get_bid_by_bank(datum)
            for datum
            in data
        ],
        meta=Meta(paginator=paginator)
    )
