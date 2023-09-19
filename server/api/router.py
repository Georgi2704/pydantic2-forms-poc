from fastapi import Depends, APIRouter
from server.api.endpoints import (  # forms,
    forms,
)

api_router = APIRouter()

api_router.include_router(
    forms.router,
    prefix="/forms",
    tags=["forms"],
)
