from fastapi import APIRouter
from apis.v1 import api_router as apiV1
from apis.v2 import api_router as apiV2


api_router = APIRouter(prefix="/api")
api_router.include_router(apiV1, prefix="/v1")
api_router.include_router(apiV2, prefix="/v2")
