from pydantic import BaseModel, EmailStr, Field


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class CreateUserSchema(LoginSchema):
    first_name: str
    last_name: str


class ConfirmEmailSchema(BaseModel):
    email: EmailStr
    confirmation_code: str


class LoginSuccessResponse(BaseModel):
    access_token: str = Field(..., validation_alias="AccessToken")
    expires_in: int = Field(..., validation_alias="ExpiresIn")
    token_type: str = Field(..., validation_alias="TokenType")
    refresh_token: str = Field(..., validation_alias="RefreshToken")
    id_token: str = Field(..., validation_alias="IdToken")
