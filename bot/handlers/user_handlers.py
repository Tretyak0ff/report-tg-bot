from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart
# from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboard_utils import _create_inline_keyboard
from models.database import User
from loguru import logger
from middlewares.user import MessageMiddleware


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
                "text": "📝 Добавить отчет",
                "value": f'{user.work_mode}'},
            {"action": "btn_profile",
                "text": "🥷 Просмотр профиля",
                "value": f'{user.work_mode}'}
        ))


@router.message(Command(commands='menu'))
async def _menu(message: Message, user: User):
    await message.answer(
        text=LEXICON_RU['/menu'],
        reply_markup=_create_inline_keyboard(
            1,
            {"action": "btn_report",
             "text": "📝 Добавить отчет",
             "value": f'{user.work_mode}'},
            {"action": "btn_profile",
             "text": "🥷 Просмотр профиля",
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
                btn_back="⬅ Назад"))
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
                btn_back="⬅ Назад"))
    else:
        await message.answer(
            text=LEXICON_RU['/work_mode'],
            reply_markup=_create_inline_keyboard(
                width=2,
                btn_mode_five="5⃣ Пятидневный",
                btn_mode_shift="🔁 Сменный",
                btn_menu="🗂 Меню"))

# @router.message(AddReport._user_data)
# async def _check_user_data(message: Message, session: AsyncSession,
#                            state: FSMContext, user: User):
#     logger.error('!!!!!   Алоха   !!!!!')
    # await state.update_data(task=message.text)
    # await _create_task(session=session, user=user, task=message.text)
    # await DeleteMessage(chat_id=message.chat.id,
    #                     message_id=message.message_id-1)
    # await message.answer(
    #     text=LEXICON_RU['/add_task'],
    #     reply_markup=_create_inline_keyboard(
    #         width=2,
    #         btn_compelete_report="✅ Завершить"))


@router.message()
async def _echo(message: Message):
    logger.debug(message.text)
    await message.reply(['/menu'], reply_markup=ReplyKeyboardMarkup())
    await message.answer(text=LEXICON_RU['/echo'])
    # try:
    #     await message.send_copy(chat_id=message.chat.id)
    # except TypeError:
    #     await message.reply(text=LEXICON_RU['no_echo'])
