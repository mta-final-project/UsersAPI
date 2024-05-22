import uvicorn

from src.core.settings import get_settings
from src.core.app import app


if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(app, host=settings.api.host, port=settings.api.port, log_level="info")
