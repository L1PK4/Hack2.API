from typing import Literal

from app import crud, deps, getters, models, schemas
from app.exceptions import UnfoundEntity, UnprocessableEntity
from app.utils.auth_session.deps import in_auth_session
from app.utils.auth_session.schemas import GettingAuthSession
from app.utils.logging import lprint
from app.utils.response import get_responses_description_by_codes
from fastapi import APIRouter, Depends, File, Path, Query, UploadFile
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    '/universities/',
    tags=["Клиентское приложение / Университеты"],
    name="Получить всех университеты",
    response_model=schemas.response.ListOfEntityResponse[schemas.university.GettingUniversity],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_universities(
        db: Session = Depends(deps.get_db),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_university.university.get_page(
        db=db, pag=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.university.get_university(university=university)
            for university in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/universities/',
    tags=["Панель Управления / Университеты"],
    name="Получить всех университеты",
    response_model=schemas.response.ListOfEntityResponse[schemas.university.GettingUniversity],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_universities(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_university.university.get_page(
        db=db, pag=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.university.get_university(university=university)
            for university in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/universities/{university_id}/',
    tags=["Панель Управления / Университеты"],
    name="Получить пользователя по идентификатору",
    response_model=schemas.response.SingleEntityResponse[schemas.university.GettingUniversity],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_university_by_id(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        university_id: int = Path(...)
):
    university = crud.crud_university.university.get(db=db, id=university_id)
    if university is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    return schemas.response.SingleEntityResponse(
        data=getters.university.get_university(university=university)
    )


@router.post(
    '/cp/universities/',
    tags=["Панель Управления / Университеты"],
    name="создать Университет",
    response_model=schemas.response.SingleEntityResponse[schemas.university.GettingUniversity],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def create_university(
        data: schemas.university.CreatingUniversity,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
):
    university = crud.crud_university.university.create(db=db, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.university.get_university(university=university)
    )


@router.put(
    '/cp/universities/{university_id}/',
    tags=["Панель Управления / Университеты"],
    name="изменить университет",
    response_model=schemas.response.SingleEntityResponse[schemas.university.GettingUniversity],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def edit_university(
        data: schemas.university.UpdatingUniversity,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        university_id: int = Path(...),
):
    university = crud.crud_university.university.get(db=db, id=university_id)
    if university is None:
        raise UnfoundEntity(message="Универ не найден", num=1)

    university = crud.crud_university.university.update(
        db=db, db_obj=university, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.university.get_university(university=university)
    )


@router.delete(
    '/cp/universities/{university_id}/',
    tags=["Панель Управления / Университеты"],
    name="удалить унивеситет",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403, 400])
)
def delete_university(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        university_id: int = Path(...),
):
    crud.crud_university.university.remove_by_id(db=db, id=university_id)

    return schemas.response.OkResponse()


@router.put(
    '/cp/universities/{university_id}/photo/',
    tags=["Панель Управления / Университеты"],
    name="изменить фото университета",
    response_model=schemas.response.SingleEntityResponse[schemas.university.GettingUniversity],
    responses=get_responses_description_by_codes([401, 403, 400, 404]),
)
def change_photo(
    db: Session = Depends(deps.get_db),
    new_photo: UploadFile | None = File(None),
    university_id: int = Path(...),
    current_user: models.User = Depends(
        in_auth_session(deps.get_current_active_superuser)),
):
    university = crud.crud_university.university.get(db=db, id=university_id)

    if university is None:
        raise UnfoundEntity("Универ не найден", num=1)

    result = crud.university.change_content(
        db=db,
        obj=university,
        content=new_photo
    )
    if result != 0:
        raise UnprocessableEntity("Не удалось изменить фото")

    return schemas.response.SingleEntityResponse(
        data=getters.university.get_university(university=university)
    )
