import boto3

from src.core.settings import get_settings
from src.services.cognito_schemas import (
    CreateUserSchema,
    ConfirmEmailSchema,
    LoginSchema,
)


class CognitoService:
    def __init__(self):
        self.client = boto3.client("cognito-idp", region_name="us-east-1")
        self.client_id = get_settings().cognito.client_id

    def register(self, params: CreateUserSchema) -> None:
        response = self.client.sign_up(
            ClientId=self.client_id,
            Username=params.email,
            Password=params.password,
            UserAttributes=[
                {"Name": "given_name", "Value": params.first_name},
                {"Name": "family_name", "Value": params.last_name},
            ],
        )
        print(response)

    def confirm_email(self, params: ConfirmEmailSchema) -> None:
        response = self.client.confirm_sign_up(
            ClientId=self.client_id,
            Username=params.email,
            ConfirmationCode=params.confirmation_code,
        )
        print(response)

    def login(self, params: LoginSchema) -> None:
        response = self.client.initiate_auth(
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": params.email, "PASSWORD": params.password},
            ClientId=self.client_id,
        )
        print(response)
