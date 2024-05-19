import boto3

from src.core.settings import get_settings
from src.services.cognito_schemas import CognitoUser


def register(user: CognitoUser) -> None:
    client = boto3.client("cognito-idp", region_name="us-east-1")
    response = client.sign_up(
        ClientId=get_settings().cognito.client_id,
        Username=user.email,
        Password=user.password,
        UserAttributes=[
            {"Name": "given_name", "Value": user.first_name},
            {"Name": "family_name", "Value": user.last_name},
        ],
    )
    print(response)
