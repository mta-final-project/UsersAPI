import uvicorn
from app.settings import get_settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings import get_settings
from app.endpoints import router

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        "app.app:app", host=settings.api.host, port=settings.api.port, log_level="info"
    )
