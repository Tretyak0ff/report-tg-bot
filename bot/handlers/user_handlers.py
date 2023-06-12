from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from models.user import User

router: Router = Router()


@router.message(CommandStart())
async def _start(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name}!\n\n'
        f'Команда /help ознакомление с возможностями'
    )


@router.message(Command(commands='help'))
async def _help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='report'))
async def _report(message: Message, session: AsyncSession):
    logger.info(message.date)
    logger.warning(session)
    await message.answer(text='здесь будет FMS')
    await session.merge(
        User(
            telegram_user_id=message.from_user.id,
            created_at=message.date,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            is_superuser=False
        ))
    await session.commit()


@router.message()
async def _echo(message: Message):
    try:
        # logger.info(message.date)
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
