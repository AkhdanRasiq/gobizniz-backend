from fastapi import APIRouter
from apis.v1 import route_accounts


api_router = APIRouter()
api_router.include_router(route_accounts.route, prefix="/account", tags=["accounts"])
