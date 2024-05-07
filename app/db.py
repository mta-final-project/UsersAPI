import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase
from app.settings import get_settings

settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.mongo.url, uuidRepresentation="standard"
)
db = client[settings.mongo.database]


class User(BeanieBaseUser, Document):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
