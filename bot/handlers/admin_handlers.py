from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
# from lexicon.lexicon_ru import LEXICON_RU
from loguru import logger

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    logger.warning(message.from_user)
    await message.answer(text='Бот запущен')
