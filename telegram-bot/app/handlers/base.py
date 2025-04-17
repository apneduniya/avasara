from aiogram import types

from app.bot_controller.router import Router
from app.services.server.contract import ContractService
from app.core.config import config


base_router = Router(name=__name__)
contract_service = ContractService()


@base_router.register(
    command="start",
    description="Start the bot",
)
async def send_welcome(message: types.Message):
    username = message.from_user.username
    is_user_registered = contract_service.is_user_exists(username)

    if is_user_registered:
        return [
            f"Hello {username}! I'm Avasara!\nI collect best opportunities from different sources just for you!",
            "Thank you for choosing us!"
        ]

    return [
        f"Hello {username}! I'm Avasara!\nI collect best opportunities from different sources just for you!",
        "You can use /register command to create an account."
    ]


@base_router.register(
    command="help",
    description="View all available commands",
)
async def help(message: types.Message):
    all_commands = Router.get_all_commands()
    if not all_commands:
        return "No commands available."
    return "Available commands:\n" + "\n".join(all_commands)


# @base_router.register()
# async def common(message: types.Message):
#     print("\ncommon\n")




