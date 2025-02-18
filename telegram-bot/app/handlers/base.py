from aiogram import types

from app.bot_controller.router import Router


router = Router(name=__name__)


@router.register(
    command="start",
    description="Start the bot",
)
async def send_welcome(message: types.Message):
    return "Hello! I'm Awasara!\nI collect best opportunities from different sources just for you!"


@router.register(
    command="help",
    description="View all available commands",
)
async def help(message: types.Message):
    return "\n".join(router.command_list)




