from aiogram import Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from aiogram.methods import EditMessageText
from aiogram.fsm.context import FSMContext

from middlewares.user import CallbackMiddleware
from keyboards.keyboard_utils import _create_inline_keyboard
from states.user import AddTask

# from lexicon.lexicon_ru import LEXICON_RU
# from keyboards.keyboard_utils import _create_inline_keyboard
# from models.user import _get_user
# from loguru import logger
# from filters.user import FilterUser


router: Router = Router()
router.callback_query.middleware(CallbackMiddleware())


@router.callback_query(Text(text=["btn_view_report"]))
async def _btn_view_report_press(callback: CallbackQuery, message_text: str):
    await EditMessageText(text=message_text + "\n🔭",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await callback.message.answer(
        text="Просмотр задач",
        reply_markup=_create_inline_keyboard(
            width=1,
            btn_back="⬅️ Назад"))


@router.callback_query(Text(text=["btn_add_report"]))
async def _btn_add_report_press(callback: CallbackQuery, message_text: str,
                                state: FSMContext):
    await EditMessageText(text=message_text + "\n➕",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)

    await state.set_state(AddTask.task)
    # await callback.message.answer(
    #     text="Добавление отчета",
    #     reply_markup=_create_inline_keyboard(
    #         width=1,
    #         btn_back="⬅️ Назад"))


# @router.callback_query(Checks._user)
# @router.callback_query(Text(text=["btn_add_report"]))
# async def _btn_add_report_press(callback: CallbackQuery, state: FSMContext,
#                                 session: AsyncSession):
#     user: User = await _get_user(aiogram_user=callback.from_user,
#                                  session=session)
#     await state.update_data(task=message.text)
#     logger.error(user.__dict__)
# logger.debug("_btn_add_report_press")
# await state.set_state(AddReport._user_data)
# u
# if user.work_mode:
#     await callback.message.edit_text(
#         text=LEXICON_RU['/add_report'],
#         reply_markup=_create_inline_keyboard(width=2,
#                                              btn_add_report_back="⬅ Назад"))
#     await state.set_state(AddTask.task)
# else:
#     logger.error("no work mode")
# return user


# @router.callback_query(Text(text=["btn_edit_profile"]))
# @router.callback_query(Text(text=["btn_add_report"]), AbsenceWorkMode())
# async def _btn_add_report_press_absence(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=LEXICON_RU['/add_work_mode'],
#         reply_markup=_create_inline_keyboard(width=2,
#                                              btn_mode_five="💀 Пятидневный",
#                                              btn_mode_shift="☠️ Сменный",
#                                              btn_back="⬅ Назад"))


# @router.callback_query(Text(text=["btn_mode_five"]), FilterUser())
# async def _btn_mode_five_press(callback: CallbackQuery, user: User,
#                                session: AsyncSession):
#     logger.debug("_btn_mode_five_press")
#     user.work_mode = "five-day"
#     await session.commit()
#     await callback.message.edit_text(
#         text=LEXICON_RU['/report'],
#         reply_markup=_create_inline_keyboard(
#             width=2,
#             btn_add_report="➕ Добавить",
#             btn_view_report="🔭 Посмотреть",
#             btn_back="⬅ Назад"))


# @router.callback_query(Text(text=["btn_mode_shift"]), FilterUser())
# async def _btn_mode_shift_press(callback: CallbackQuery, user: User,
#                                 session: AsyncSession):
#     user.work_mode = "shift"
#     await session.commit()
#     logger.debug("_btn_mode_shift_press")

#     await callback.message.edit_text(
#         text=LEXICON_RU['/report'],
#         reply_markup=_create_inline_keyboard(
#             width=2,
#             btn_add_report="➕ Добавить",
#             btn_view_report="🔭 Посмотреть",
#             btn_back="⬅ Назад"))


# @router.callback_query(Text(text=["btn_add_report_back"]))
# async def _btn_add_report_back_press(callback: CallbackQuery,
#                                      state: FSMContext):
#     await callback.message.edit_text(
#         text=LEXICON_RU['/report'],
#         reply_markup=_create_inline_keyboard(width=2,
#                                              btn_add_report="➕ Добавить",
#                                              btn_view_report="🔭 Посмотреть",
#                                              btn_back="⬅ Назад"))
#     await state.clear()


# @router.callback_query(Text(text=["btn_compelete_report"]))
# async def _btn_compelete_report_press(callback: CallbackQuery,
#                                       state: FSMContext):
#     await state.clear()
#     await callback.message.edit_text(
#         text=LEXICON_RU['/compelete_report'],
#         reply_markup=_create_inline_keyboard(width=2,
#                                              btn_add_report="➕ Добавить",
#                                              btn_view_report="🔭 Посмотреть",
#                                              btn_back="⬅ Назад"))
