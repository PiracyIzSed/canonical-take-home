from fastapi import FastAPI

from sqlalchemy.ext.asyncio import create_async_engine
from starlette.middleware.cors import CORSMiddleware

from app.core.settings.app import AppSettings

def get_application(settings: AppSettings) -> FastAPI:
    
    settings.configure_logging()
    app = FastAPI(**settings.fastapi_kwargs)
    app.add_middleware(CORSMiddleware, allow_origins=settings.allowed_hosts, allow_credentials=True)
    
    @app.on_event("startup")
    def connect_to_db():
        engine = create_async_engine(settings.database_url)
        app.state.engine = engine


    @app.on_event("shutdown")
    def disconnect_from_db():
        app.state.engine.close()
    return app
