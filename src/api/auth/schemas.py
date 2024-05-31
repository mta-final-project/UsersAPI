from typing import Any

from pydantic import BaseModel


type JWK = dict[str, str]


class JWKS(BaseModel):
    keys: list[JWK]


class JWTAuthCredentials(BaseModel):
    jwt_token: str
    header: dict[str, str]
    claims: dict[str, Any]
    signature: str
    message: str
