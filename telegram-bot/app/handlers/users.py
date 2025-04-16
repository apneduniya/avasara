from aiogram import types

from app.bot_controller.router import Router
from app.services.server.contract import ContractService
from app.core.config import config


users_router = Router(name=__name__)
contract_service = ContractService()


@users_router.register(
    command="register",
    description="Register an account",
)
async def register(message: types.Message):
    username = message.from_user.username
    is_user_registered = contract_service.is_user_exists(username)

    if is_user_registered:
        return "You are already registered!"

    return f"Please visit {config.FRONTEND_URL}/register to create an account."