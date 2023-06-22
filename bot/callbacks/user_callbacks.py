from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.user import _create_inline_keyboard
from states.user import AddTask


router: Router = Router()


@router.callback_query(Text(text=["btn_help"]))
async def _btn_help_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/help'],
        reply_markup=_create_inline_keyboard(
            2,
            btn_report="📝 Отчет")
    )


@router.callback_query(Text(text=["btn_report"]))
async def _btn_report_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/report'],
        reply_markup=_create_inline_keyboard(
            2,
            btn_add_report="➕ Добавить",
            btn_view_report="🔭 Посмотреть")
    )


@router.callback_query(Text(text=["btn_add_report"]))
async def _btn_add_reprot_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=LEXICON_RU['/add_report'])
    await state.set_state(AddTask.task)


@router.callback_query(Text(text=["btn_compelete_report"]))
async def _btn_compelete_report_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/compelete_report'],
        reply_markup=_create_inline_keyboard(
            2,
            btn_add_report="➕ Добавить",
            btn_view_report="🔭 Посмотреть")
    )
