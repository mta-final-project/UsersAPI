from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8002


class CognitoSettings(BaseModel):
    client_id: str = "7vsgt6q02n2pl4dfb362pvarlg"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter="__")

    api: ApiSettings = ApiSettings()
    cognito: CognitoSettings = CognitoSettings()


@lru_cache
def get_settings():
    return Settings()
