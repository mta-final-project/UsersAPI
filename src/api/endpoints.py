from typing import Annotated, Any

from fastapi import APIRouter, status, Depends

from src.api.schemas import LoginSchema, ConfirmEmailSchema, CreateUserSchema
from src.api.service import CognitoService
from src.api.deps import cognito_service

router = APIRouter(prefix="", tags=["auth"])

ServiceDep = Annotated[
    CognitoService,
    Depends(cognito_service),
]


@router.post("/register", status_code=status.HTTP_200_OK)
async def register(params: CreateUserSchema, service: ServiceDep) -> Any:
    return service.register(params)


@router.post("/confirm-email", status_code=status.HTTP_200_OK)
async def confirm_email(params: ConfirmEmailSchema, service: ServiceDep) -> Any:
    return service.confirm_email(params)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(params: LoginSchema, service: ServiceDep) -> Any:
    return service.login(params)
