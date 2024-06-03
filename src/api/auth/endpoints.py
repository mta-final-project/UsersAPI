from fastapi import APIRouter, status, Depends

from src.core.auth import JWTAuthCredentials, JWTBearer

router = APIRouter(prefix="/auth", tags=["auth"])

auth = JWTBearer()


@router.post("/validate", status_code=status.HTTP_204_NO_CONTENT)
async def validate_token(
    _credentials: JWTAuthCredentials = Depends(auth),
) -> None: ...
