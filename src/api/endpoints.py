from typing import Annotated

from fastapi import APIRouter, status, Depends

from src.api.schemas import LoginSchema, ConfirmEmailSchema, CreateUserSchema, LoginSuccessResponse
from src.api.service import CognitoService
from src.api.deps import cognito_service

router = APIRouter(prefix="", tags=["auth"])

ServiceDep = Annotated[
    CognitoService,
    Depends(cognito_service),
]


@router.post("/register", status_code=status.HTTP_204_NO_CONTENT)
async def register(params: CreateUserSchema, service: ServiceDep) -> None:
    service.register(params)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(params: LoginSchema, service: ServiceDep) -> LoginSuccessResponse:
    return service.login(params)
