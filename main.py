import uvicorn
from app.settings import get_settings

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        "app.app:app", host=settings.api.host, port=settings.api.port, log_level="info"
    )
