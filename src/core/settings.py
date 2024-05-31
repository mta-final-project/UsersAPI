from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8002


class CognitoSettings(BaseModel):
    client_id: str = "6r70ag4thnsitfb378fh87tj92"
    pool_id: str = "us-east-1_U2F78N1y3"
    region: str = "us-east-1"
    jwk_url: str = (
        f"https://cognito-idp.{region}.amazonaws.com/{pool_id}/.well-known/jwks.json"
    )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    api: ApiSettings = ApiSettings()
    cognito: CognitoSettings = CognitoSettings()


@lru_cache
def get_settings():
    return Settings()
