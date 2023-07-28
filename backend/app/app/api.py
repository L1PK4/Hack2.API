from app.endpoints import (email_verification_code, faculty, login,
                           tel_verification_code, users)
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(email_verification_code.router)
api_router.include_router(tel_verification_code.router)
api_router.include_router(faculty.router)
