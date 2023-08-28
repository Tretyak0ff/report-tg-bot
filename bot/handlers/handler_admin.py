from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router: Router = Router()


@router.message(CommandStart())
async def _start(message: Message):
    await message.answer(
        text=f'{message.from_user.username} bot is running...'
    )
