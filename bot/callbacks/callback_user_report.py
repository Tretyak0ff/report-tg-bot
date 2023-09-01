from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.methods import EditMessageText
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession


from keyboards.keyboard_utils import _create_inline_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from middlewares.user import CallbackMiddleware
from states.user import AddTask
from models.database import User
from models.user import _view_report


# from loguru import logger


router: Router = Router()
router.callback_query.middleware(CallbackMiddleware())


@router.callback_query(Text(text=["btn_view_report"]))
async def _btn_view_report_press(callback: CallbackQuery,
                                 message_text: str,
                                 session: AsyncSession,
                                 user: User):
    await EditMessageText(text=message_text + "\n🔭",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await _view_report(user=user, session=session)
    await callback.message.answer(
        text="Просмотр задач:",
        reply_markup=_create_inline_keyboard(
            width=1,
            btn_back="⬅️ Назад"))


@router.callback_query(Text(text=["btn_add_report"]))
async def _btn_add_report_press(callback: CallbackQuery,
                                message_text: str,
                                state: FSMContext):
    await EditMessageText(text=message_text + "\n➕",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await callback.message.answer(
        text=LEXICON_RU['/add_report'],
        reply_markup=_create_inline_keyboard(
            width=1,
            btn_back="⬅️ Назад"))
    await state.set_state(AddTask.task)


@router.callback_query(Text(text=["btn_compelete_report"]))
async def _btn_report_press(callback: CallbackQuery,
                            state: FSMContext,
                            message_text: str):
    await EditMessageText(text=message_text + "\n✅",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await state.clear()
    await callback.message.answer(
        text=LEXICON_RU['/report'],
        reply_markup=_create_inline_keyboard(
            width=2,
            btn_add_report="➕ Добавить",
            btn_view_report="🔭 Посмотреть",
            btn_menu="🗂 Меню"))
