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
    '/faculties/',
    tags=["Клиентское приложение / Факультеты"],
    name="Получить всех факультеты",
    response_model=schemas.response.ListOfEntityResponse[schemas.faculty.GettingFaculty],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_faculties(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_user)),
        city_id: int | None = Query(None),
        cost_from: int | None = Query(None),
        cost_to: int | None = Query(None),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_faculty.faculty.get_page(
        db=db,
        page=page,
        cost_range=[cost_from, cost_to],
        city_id=city_id
    )

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.faculty.get_faculty(
                faculty=faculty, db=db, user=current_user)
            for faculty in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/cp/faculties/',
    tags=["Панель Управления / Факультеты"],
    name="Получить всех факультеты",
    response_model=schemas.response.ListOfEntityResponse[schemas.faculty.GettingFaculty],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def get_all_faculties(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        page: int | None = Query(None)
):
    data, paginator = crud.crud_faculty.faculty.get_page(
        db=db, page=page)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.faculty.get_faculty(faculty=faculty)
            for faculty in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.get(
    '/faculties/{faculty_id}/',
    tags=["Клиентское приложение / Факультеты"],
    name="Получить пользователя по идентификатору",
    response_model=schemas.response.SingleEntityResponse[schemas.faculty.GettingFaculty],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_faculty_by_id(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        faculty_id: int = Path(...)
):
    faculty = crud.crud_faculty.faculty.get(db=db, id=faculty_id)
    if faculty is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    return schemas.response.SingleEntityResponse(
        data=getters.faculty.get_faculty(
            faculty=faculty, db=db, user=current_user)
    )


@router.post(
    '/cp/faculties/',
    tags=["Панель Управления / Факультеты"],
    name="создать пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.faculty.GettingFaculty],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def create_faculty(
        data: schemas.faculty.CreatingFaculty,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
):
    faculty = crud.crud_faculty.faculty.create(db=db, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.faculty.get_faculty(faculty=faculty)
    )


@router.put(
    '/cp/faculties/{faculty_id}/',
    tags=["Панель Управления / Факультеты"],
    name="изменить пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.faculty.GettingFaculty],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def edit_faculty(
        data: schemas.faculty.UpdatingFaculty,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        faculty_id: int = Path(...),
):
    faculty = crud.crud_faculty.faculty.get(db=db, id=faculty_id)
    if faculty is None:
        raise UnfoundEntity(message="Пользователь не найден", num=1)

    faculty = crud.crud_faculty.faculty.update(
        db=db, db_obj=faculty, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.faculty.get_faculty(faculty=faculty)
    )


@router.delete(
    '/cp/faculties/{faculty_id}/',
    tags=["Панель Управления / Факультеты"],
    name="удалить пользователя",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403, 400])
)
def delete_faculty(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(
            in_auth_session(deps.get_current_active_superuser)),
        faculty_id: int = Path(...),
):
    crud.crud_faculty.faculty.remove_by_id(db=db, id=faculty_id)

    return schemas.response.OkResponse()
