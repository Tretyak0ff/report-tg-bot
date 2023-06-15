from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon_ru import LEXICON_RU
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from services.user import _get_or_create_user
from keyboards.user import create_inline_keyboard

from aiogram.filters import Text

router: Router = Router()


@router.message(CommandStart())
async def _start(message: Message):
    await message.answer(
        text=f"Привет, {message.from_user.full_name}!\n\n"
        f"{ LEXICON_RU['/start']}",
        reply_markup=create_inline_keyboard(2, btn_help="🆘 Помощь")
    )


@router.callback_query(Text(text=["btn_help"]))
async def _button_help_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/help'],
        reply_markup=create_inline_keyboard(2, btn_report="📝 Отчет")
    )


@router.callback_query(Text(text=["btn_report"]))
async def _button_report_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Нажата кнопка Добавить отчет"
    )


@router.message(Command(commands='help'))
async def _help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='report'))
async def _report(message: Message, session: AsyncSession):
    logger.info(message.date)
    logger.warning(session)
    await message.answer(text='здесь будет FMS')
    logger.debug(await _get_or_create_user(message=message, session=session))


@router.message()
async def _echo(message: Message):
    try:
        # logger.info(message.date)
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
