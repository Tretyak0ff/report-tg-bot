from aiogram import F, Router
from aiogram.filters import Text
from aiogram.types import CallbackQuery
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboard_utils import _create_inline_keyboard
from models.database import User
from keyboards.keyboard_utils import UserCallback
from middlewares.user import CallbackMiddleware
from aiogram.methods import EditMessageText
from aiogram.fsm.context import FSMContext

router: Router = Router()
router.callback_query.middleware(CallbackMiddleware())


@router.callback_query(Text(text=["btn_menu"]))
async def btn_back_press(callback: CallbackQuery, user: User,
                         message_text: str):
    await EditMessageText(text=message_text + "\n🗂",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await callback.message.answer(
        text=LEXICON_RU['/menu'],
        reply_markup=_create_inline_keyboard(
            1,
            {"action": "btn_report",
             "text": "📝 Отчет",
             "value": f'{user.work_mode}'},
            {"action": "btn_profile",
             "text": "🥷 Профиль",
             "value": f'{user.work_mode}'}
        )
    )


@router.callback_query(UserCallback.filter(F.value == "None"))
async def _press_new_user(callback: CallbackQuery, message_text: str):
    await EditMessageText(text=message_text + "\n<i>⛔ "
                          "Не указан режим работы</i>",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await callback.message.answer(text=LEXICON_RU['/work_mode'],
                                  reply_markup=_create_inline_keyboard(
        width=2,
        btn_mode_five="5⃣ Пятидневный",
        btn_mode_shift="🔁 Сменный",
        btn_menu="🗂 Меню"))


@router.callback_query(UserCallback.filter(F.action == "btn_report"))
@router.callback_query(Text(text=["btn_back"]))
async def _btn_report_press(callback: CallbackQuery, state: FSMContext,
                            message_text: str):
    await state.clear()
    await EditMessageText(text=message_text + "\n📝",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await callback.message.answer(text=LEXICON_RU['/report'],
                                  reply_markup=_create_inline_keyboard(
        width=2,
        btn_add_report="➕ Добавить",
        btn_view_report="🔭 Посмотреть",
        btn_menu="🗂 Меню"))


@router.callback_query(UserCallback.filter(F.action == "btn_profile"))
async def _btn_profile_press(callback: CallbackQuery, user: User,
                             message_text: str):
    await EditMessageText(text=message_text + "\n🥷",
                          chat_id=callback.message.chat.id,
                          message_id=callback.message.message_id)
    await callback.message.answer(text=LEXICON_RU['/profile'] +
                                  f"{await user._print()}",
                                  reply_markup=_create_inline_keyboard(
                                      width=1,
                                      btn_edit_profile="✏ Редактировать",
                                      btn_menu="🗂 Меню"))
