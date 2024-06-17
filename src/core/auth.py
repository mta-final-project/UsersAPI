from typing import Any
import httpx
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, jwk, JWTError
from jose.utils import base64url_decode
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel

from src.core.settings import get_settings

type JWK = dict[str, str]


class JWKS(BaseModel):
    keys: list[JWK]


class JWTAuthCredentials(BaseModel):
    jwt_token: str
    header: dict[str, str]
    claims: dict[str, Any]
    signature: str
    message: str


def get_jwk() -> JWKS:
    response = httpx.get(get_settings().cognito.jwk_url)

    return JWKS.parse_obj(response.json())


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

        jwks = get_jwk()
        self.kid_to_jwk = {key["kid"]: key for key in jwks.keys}

    async def __call__(self, request: Request) -> JWTAuthCredentials | None:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials is None:
            return None

        jwt_credentials = self.extract_credentials(credentials)

        if not self.verify_jwk_token(jwt_credentials):
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="JWK invalid")

        return jwt_credentials

    def verify_jwk_token(self, jwt_credentials: JWTAuthCredentials) -> bool:
        kid = jwt_credentials.header.get("kid")
        if not kid:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="no kid found in JWT header"
            )

        public_key = self.kid_to_jwk.get(kid)
        if not public_key:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="JWK public key not found"
            )

        key = jwk.construct(public_key)
        decoded_signature = base64url_decode(jwt_credentials.signature.encode())

        return key.verify(jwt_credentials.message.encode(), decoded_signature)

    @classmethod
    def extract_credentials(
        cls, credentials: HTTPAuthorizationCredentials
    ) -> JWTAuthCredentials | None:
        cls.verify_auth_method(credentials)
        jwt_token = credentials.credentials

        if "." not in jwt_token:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Invalid JWT token"
            )

        message, signature = jwt_token.rsplit(".", 1)

        try:
            return JWTAuthCredentials(
                jwt_token=jwt_token,
                header=jwt.get_unverified_header(jwt_token),
                claims=jwt.get_unverified_claims(jwt_token),
                signature=signature,
                message=message,
            )
        except JWTError:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="JWK invalid")

    @staticmethod
    def verify_auth_method(credentials: HTTPAuthorizationCredentials) -> None:
        if not credentials.scheme == "Bearer":
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Wrong authentication method"
            )
