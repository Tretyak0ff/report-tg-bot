from aiogram import F, Router
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.keyboard_utils import _create_inline_keyboard
from lexicon.lexicon_ru import LEXICON_RU
from middlewares.user import CallbackMiddleware
from models.database import User
from models.user import _update_user


router: Router = Router()
router.callback_query.middleware(CallbackMiddleware())


@router.callback_query(F.data == "btn_edit_profile")
async def btn_edit_profile_press(callback: CallbackQuery, message_text: str):
    await callback.message.edit_text(text=message_text + "\n✏")
    await callback.message.answer(text=LEXICON_RU['/work_mode'],
                                  reply_markup=_create_inline_keyboard(
        width=2,
        btn_mode_five="5⃣ Пятидневный",
        btn_mode_shift="🔁 Сменный",
        btn_menu="🗂 Меню"))


@router.callback_query(F.data == "btn_mode_five")
async def btn_mode_five_press(callback: CallbackQuery,
                              message_text: str,
                              session: AsyncSession,
                              user: User):
    user.work_mode = "five-day"
    await _update_user(session=session,
                       aiogram_user=callback.from_user,
                       user=user)
    await callback.message.edit_text(text=message_text + "\n5⃣")
    await callback.message.answer(
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


@router.callback_query(F.data == "btn_mode_shift")
async def btn_mode_shift_press(callback: CallbackQuery,
                               message_text: str,
                               session: AsyncSession,
                               user: User):
    user.work_mode = "shift"
    await _update_user(session=session,
                       aiogram_user=callback.from_user,
                       user=user)
    await callback.message.edit_text(text=message_text + "\n🔁")
    await callback.message.answer(
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
