import boto3

from src.api.schemas import (
    CreateUserSchema,
    ConfirmEmailSchema,
    LoginSchema,
)


class CognitoService:
    def __init__(self, client: boto3.client, client_id: str):
        self._client = client
        self._client_id = client_id

    def register(self, params: CreateUserSchema) -> None:
        _ = self._client.sign_up(
            ClientId=self._client_id,
            Username=params.email,
            Password=params.password,
            UserAttributes=[
                {"Name": "given_name", "Value": params.first_name},
                {"Name": "family_name", "Value": params.last_name},
            ],
        )

    def confirm_email(self, params: ConfirmEmailSchema) -> Any:
        _ = self._client.confirm_sign_up(
            ClientId=self._client_id,
            Username=params.email,
            ConfirmationCode=params.confirmation_code,
        )

    def login(self, params: LoginSchema) -> dict:
        response = self._client.initiate_auth(
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": params.email, "PASSWORD": params.password},
            ClientId=self._client_id,
        )
        return response["AuthenticationResult"]
