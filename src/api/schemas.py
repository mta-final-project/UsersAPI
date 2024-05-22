from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class CreateUserSchema(LoginSchema):
    first_name: str
    last_name: str


class ConfirmEmailSchema(BaseModel):
    email: EmailStr
    confirmation_code: str
