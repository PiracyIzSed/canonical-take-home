from fastapi import APIRouter

from app.api.routes.games.game_resource import router as games_router
from app.api.routes.users.user_resource import router as users_router

router = APIRouter()
router.include_router(users_router, tags=["users"], prefix="/users")
router.include_router(games_router, tags=["games"], prefix="/games")
