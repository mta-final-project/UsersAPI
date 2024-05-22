from typing import Annotated, Any

from botocore.exceptions import ClientError
from fastapi import APIRouter, status, Depends, HTTPException

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
    try:
        return service.register(params)
    except ClientError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.response["Error"],
        )


@router.post("/confirm-email", status_code=status.HTTP_200_OK)
async def confirm_email(params: ConfirmEmailSchema, service: ServiceDep) -> Any:
    try:
        return service.confirm_email(params)
    except ClientError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.response["Error"],
        )


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(params: LoginSchema, service: ServiceDep) -> Any:
    try:
        return service.login(params)
    except ClientError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.response["Error"],
        )
