from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
# from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboard_utils import _create_inline_keyboard
from sqlalchemy.ext.asyncio import AsyncSession
from models.database import User
from loguru import logger

# from states.user import AddTask
# from filters.user import WorkMode
# , AbsenceWorkMode


router: Router = Router()


async def _btn_edit_profile_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/add_work_mode'],
        reply_markup=_create_inline_keyboard(
            width=2,
            btn_edit_profile_mode_five="💀 Пятидневный",
            btn_edit_profile_mode_shift="☠️ Сменный",
            btn_back="⬅ Назад"))


# @router.callback_query(Text(text=["btn_edit_profile_mode_five"]))
# async def _btn_mode_five_press(callback: CallbackQuery,
#                                session: AsyncSession,
#                                user: User):
#     user.work_mode = "five-day"
#     logger.debug(user)


# @router.callback_query(Text(text=["btn_edit_profile_mode_five"]), WorkMode())
# async def _btn_mode_five_press(callback: CallbackQuery,
#                                session: AsyncSession,
#                                user: User):
#     user.work_mode = "five-day"
#     logger.debug(user)
    # await session.commit()
    # await callback.message.edit_text(
    #     text=LEXICON_RU['/add_report'],
    #     reply_markup=_create_inline_keyboard(width=2,
    #                                          btn_back="⬅ Назад"))
