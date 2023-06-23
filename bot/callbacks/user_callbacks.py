from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.user import _create_inline_keyboard
from services.user import _get_or_create_user
from states.user import AddTask
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession


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
async def _btn_report_press(callback: CallbackQuery, session: AsyncSession):
    logger.debug(_get_or_create_user(
        aiogram_user=callback.from_user, session=session)
        )

    # await callback.message.edit_text(
    #     text=LEXICON_RU['/report'],
    #     reply_markup=_create_inline_keyboard(
    #         2,
    #         btn_add_report="➕ Добавить",
    #         btn_view_report="🔭 Посмотреть")
    # )
    # logger.debug(await _get_or_create_user(message=message, session=session))


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
