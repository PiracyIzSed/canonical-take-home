from fastapi import APIRouter

from .game_resource import sub_router

router = APIRouter()

router.include_router(sub_router, prefix="/games")