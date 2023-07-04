from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.user import _create_inline_keyboard
from states.user import AddTask
from sqlalchemy.ext.asyncio import AsyncSession
from models.database import User
from filters.user import WorkMode, AbsenceWorkMode


router: Router = Router()


@router.callback_query(Text(text=["btn_help"]))
@router.callback_query(Text(text=["btn_back_report"]))
@router.callback_query(Text(text=["btn_back_profile"]))
async def _btn_help_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/help'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_report="📝 Отчет",
                                             btn_profile="🥷 Профиль"))


@router.callback_query(Text(text=["btn_report"]))
async def _btn_report_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/report'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_add_report="➕ Добавить",
                                             btn_view_report="🔭 Посмотреть",
                                             btn_back_report="⬅ Назад"))


@router.callback_query(Text(text=["btn_profile"]))
async def _btn_profile_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f"Ваш профиль,:\n\n"
        f"{ LEXICON_RU['/profile']}",
        reply_markup=_create_inline_keyboard(
            width=1,
            btn_edit_profile="✏ Редактировать",
            btn_back_profile="⬅ Назад"))
