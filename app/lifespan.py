from contextlib import asynccontextmanager
from fastapi import FastAPI
from beanie import init_beanie
from app.users import User
from app.db import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_beanie(
        database=db,
        document_models=[
            User,
        ],
    )
    yield
