from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from sqlalchemy.ext.asyncio import create_async_engine
from starlette.middleware.cors import CORSMiddleware

from app.core.settings.app import AppSettings
from app.api.errors import http_error, validation_error
from app.api.routes import router

def get_application(settings: AppSettings) -> FastAPI:
    
    settings.configure_logging()
    app = FastAPI(**settings.fastapi_kwargs)
    app.add_middleware(CORSMiddleware, allow_origins=settings.allowed_hosts, allow_credentials=True)
    
    def connect_to_db():
        engine = create_async_engine(settings.database_url)
        app.state.engine = engine


    async def disconnect_from_db():
        await app.state.engine.dispose()

    app.add_event_handler("startup", connect_to_db)
    app.add_event_handler("shutdown", disconnect_from_db)

    app.add_exception_handler(HTTPException, http_error.http_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error.http422_error_handler)

    app.include_router(router, prefix=settings.api_prefix)
    return app
