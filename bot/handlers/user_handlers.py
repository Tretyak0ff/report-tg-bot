from aiogram import Router
from aiogram.methods import DeleteMessage
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.user import _create_inline_keyboard
from states.user import AddTask
from filters.user import WorkMode
from models.database import User
from services.profile import _user
from loguru import logger

router: Router = Router()


@router.message(CommandStart())
async def _start(message: Message):
    await message.answer(
        text=f"Привет, {message.from_user.full_name}!\n\n"
        f"{ LEXICON_RU['/start']}",
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_help="🆘 Помощь"))


@router.message(Command(commands='help'))
async def _help(message: Message):
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_report="📝 Отчет",
                                             btn_profile="🥷 Профиль"))


@router.message(Command(commands='report'))
async def _report(message: Message):
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)
    await message.answer(
        text=LEXICON_RU['/report'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_add_report="➕ Добавить",
                                             btn_view_report="🔭 Посмотреть",
                                             btn_back_report="⬅ Назад"))


@router.message(AddTask.task, WorkMode())
async def _compeleted_task(message: Message, state: FSMContext, user: User):
    await state.update_data(task=message.text)
    logger.debug(message.text)
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)
    await message.answer(
        text=LEXICON_RU['/add_task'],
        reply_markup=_create_inline_keyboard(
            width=2,
            btn_compelete_report="✅ Завершить"))


@router.message(Command(commands='profile'), WorkMode())
async def _profilet(message: Message, user: User):
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)
    await message.answer(
        text=f"{_user(user=user) }"
        f"{ LEXICON_RU['/profile']}",
        reply_markup=_create_inline_keyboard(
            width=1,
            btn_edit_profile="✏ Редактировать",
            btn_back="⬅ Назад"))


@router.message()
async def _echo(message: Message):
    await DeleteMessage(chat_id=message.chat.id,
                        message_id=message.message_id-1)
    await message.answer(text=LEXICON_RU['/echo'])
    # try:
    #     await message.send_copy(chat_id=message.chat.id)
    # except TypeError:
    #     await message.reply(text=LEXICON_RU['no_echo'])
