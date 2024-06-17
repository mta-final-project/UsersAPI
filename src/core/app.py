from botocore.exceptions import ClientError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.error_hanlers import handle_boto_error
from src.api.users.endpoints import router as users_router
from src.api.auth.endpoints import router as auth_router

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)

app.add_exception_handler(ClientError, handler=handle_boto_error)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
