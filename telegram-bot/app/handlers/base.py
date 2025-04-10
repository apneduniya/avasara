from aiogram import types

from app.bot_controller.router import Router


router = Router(name=__name__)


@router.register(
    command="start",
    description="Start the bot",
)
async def send_welcome(message: types.Message):
    return [
        "Hello! I'm Avasara!\nI collect best opportunities from different sources just for you!",
        "You can use /register command to create an account."
    ]


@router.register(
    command="help",
    description="View all available commands",
)
async def help(message: types.Message):
    return "\n".join(router.command_list)


@router.register(
    command="register",
    description="Register an account",
)
async def register(message: types.Message):
    return "Send your resume to start the registration process."


@router.register()
async def common(message: types.Message):
    ...




