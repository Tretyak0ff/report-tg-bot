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


@router.callback_query(Text(text=["btn_edit_profile"]))
async def _btn_edit_profile_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/edit_profile'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_back_profile="⬅ Назад"))
