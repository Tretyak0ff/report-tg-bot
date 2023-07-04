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


@router.callback_query(Text(text=["btn_add_report"]), WorkMode())
async def _btn_add_report_press_presence(callback: CallbackQuery,
                                         state: FSMContext):
    await callback.message.edit_text(
        text=LEXICON_RU['/add_report'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_add_report_back="⬅ Назад"))
    await state.set_state(AddTask.task)


@router.callback_query(Text(text=["btn_add_report"]), AbsenceWorkMode())
async def _btn_add_report_press_absence(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/add_work_mode'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_mode_five="💀 Пятидневный",
                                             btn_mode_shift="☠️ Сменный"))


@router.callback_query(Text(text=["btn_mode_five"]), AbsenceWorkMode())
async def _btn_mode_five_press(callback: CallbackQuery, state: FSMContext,
                               session: AsyncSession, user: User):
    user.work_mode = "five-day"
    await session.commit()
    await callback.message.edit_text(
        text=LEXICON_RU['/add_report'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_add_report_back="⬅ Назад"))
    await state.set_state(AddTask.task)


@router.callback_query(Text(text=["btn_mode_shift"]), AbsenceWorkMode())
async def _btn_mode_shift_press(callback: CallbackQuery, state: FSMContext,
                                session: AsyncSession, user: User):
    user.work_mode = "shift"
    await session.commit()
    await callback.message.edit_text(
        text=LEXICON_RU['/add_report'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_add_report_back="⬅ Назад"))
    await state.set_state(AddTask.task)


@router.callback_query(Text(text=["btn_add_report_back"]))
async def _btn_add_report_back_press(callback: CallbackQuery,
                                     state: FSMContext):
    await callback.message.edit_text(
        text=LEXICON_RU['/report'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_add_report="➕ Добавить",
                                             btn_view_report="🔭 Посмотреть",
                                             btn_back_report="⬅ Назад"))
    await state.clear()


@router.callback_query(Text(text=["btn_compelete_report"]))
async def _btn_compelete_report_press(callback: CallbackQuery,
                                      state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text=LEXICON_RU['/compelete_report'],
        reply_markup=_create_inline_keyboard(width=2,
                                             btn_add_report="➕ Добавить",
                                             btn_view_report="🔭 Посмотреть",
                                             btn_back_report="⬅ Назад"))


@router.callback_query(Text(text=["btn_view_report"]))
async def _btn_view_report_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Просмотр задач",
        reply_markup=None)
