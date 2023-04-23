from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from fastapi.middleware.cors import CORSMiddleware
from apis.base import api_router
from core.config import settings


def create_app_instance() -> FastAPI:
     if settings.IS_PRODUCTION != "true":
          return FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
     return FastAPI(
            title       = settings.PROJECT_NAME,
            version     = settings.PROJECT_VERSION,
            docs_url    = None,
            redoc_url   = None,
            openapi_url = None
        )


def middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def include_router(app: FastAPI):
    app.include_router(api_router)


def create_tables():
	Base.metadata.create_all(bind=engine)


def start_application():
    app = create_app_instance()
    middleware(app)
    include_router(app)
    create_tables()
    return app


app = start_application()
