from app.endpoints import (bank, bid, email_verification_code, faculty, field,
                           login, offer, support, tel_verification_code,
                           university, users)
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(email_verification_code.router)
api_router.include_router(tel_verification_code.router)
api_router.include_router(faculty.router)
api_router.include_router(university.router)
api_router.include_router(field.router)
api_router.include_router(bank.router)
api_router.include_router(bid.router)
api_router.include_router(offer.router)
api_router.include_router(support.router)
