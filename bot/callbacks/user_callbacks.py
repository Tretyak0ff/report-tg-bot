from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.user import _create_inline_keyboard
from filters.user import WorkMode
from models.database import User
from services.profile import _user
from loguru import logger


router: Router = Router()


@router.callback_query(Text(text=["btn_help"]))
@router.callback_query(Text(text=["btn_back"]))
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
                                             btn_back="⬅ Назад"))


@router.callback_query(Text(text=["btn_profile"]), WorkMode())
async def _btn_profile_press(callback: CallbackQuery, user: User):
    logger.debug(user.__dict__)
    await callback.message.edit_text(
        text=f"{_user(user=user) }"
        f"{ LEXICON_RU['/profile']}",
        reply_markup=_create_inline_keyboard(
            width=1,
            btn_edit_profile="✏ Редактировать",
            btn_back="⬅ Назад"))
