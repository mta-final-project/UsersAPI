from botocore.exceptions import ClientError
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.error_hanlers import handle_boto_error
from src.api.endpoints import router

app = FastAPI()

app.include_router(router)

app.add_exception_handler(ClientError, handler=handle_boto_error)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
