from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.keyboard_utils import _create_inline_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from models.database import User
from models.user import _create_task
from middlewares.user import MessageMiddleware
from states.user import AddTask


router: Router = Router()
router.message.middleware(MessageMiddleware())


@router.message(CommandStart())
async def _start(message: Message, user: User):
    await message.answer(
        text=f"<b>Привет, {message.from_user.full_name}!\n\n</b>"
        f"{LEXICON_RU['/start']}",
        reply_markup=_create_inline_keyboard(
            1,
            {"action": "btn_report",
                "text": "📝Отчет",
                "value": f'{user.work_mode}'},
            {"action": "btn_profile",
                "text": "🥷 Профиля",
                "value": f'{user.work_mode}'}
        ))


@router.message(Command(commands='menu'))
async def _menu(message: Message, user: User):
    await message.answer(
        text=LEXICON_RU['/menu'],
        reply_markup=_create_inline_keyboard(
            1,
            {"action": "btn_report",
             "text": "📝 Отчет",
             "value": f'{user.work_mode}'},
            {"action": "btn_profile",
             "text": "🥷 Профиль",
             "value": f'{user.work_mode}'}
        ))


@router.message(Command(commands='report'))
async def _report(message: Message, user: User):
    if user.work_mode:
        await message.answer(
            text=LEXICON_RU['/report'],
            reply_markup=_create_inline_keyboard(
                width=2,
                btn_add_report="➕ Добавить",
                btn_view_report="🔭 Посмотреть",
                btn_menu="🗂 Меню"))
    else:
        await message.answer(
            text=LEXICON_RU['/work_mode'],
            reply_markup=_create_inline_keyboard(
                width=2,
                btn_mode_five="5⃣ Пятидневный",
                btn_mode_shift="🔁 Сменный",
                btn_menu="🗂 Меню"))


@router.message(Command(commands='profile'))
async def _profile(message: Message, user: User):
    if user.work_mode:
        await message.answer(
            text=f"{await user._print()}",
            reply_markup=_create_inline_keyboard(
                width=1,
                btn_edit_profile="✏ Редактировать",
                btn_menu="🗂 Меню"))
    else:
        await message.answer(
            text=LEXICON_RU['/work_mode'],
            reply_markup=_create_inline_keyboard(
                width=2,
                btn_mode_five="5⃣ Пятидневный",
                btn_mode_shift="🔁 Сменный",
                btn_menu="🗂 Меню"))


@router.message(AddTask.task)
async def _add_task(message: Message, session: AsyncSession,
                    state: FSMContext, user: User):
    await state.update_data(task=message.text)
    await _create_task(session=session, user=user, task=message.text)
    await message.answer(
        text=LEXICON_RU['/add_task'],
        reply_markup=_create_inline_keyboard(
            width=1,
            btn_compelete_report="✅ Завершить"))


@router.message()
async def _echo(message: Message):
    await message.answer(text=LEXICON_RU['/echo'])
    # try:
    #     await message.send_copy(chat_id=message.chat.id)
    # except TypeError:
    #     await message.reply(text=LEXICON_RU['no_echo'])
