from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
# from services.user import _get_or_create_user
from keyboards.user import _create_inline_keyboard
from states.user import AddTask


router: Router = Router()


@router.message(CommandStart())
async def _start(message: Message):
    await message.answer(
        text=f"Привет, {message.from_user.full_name}!\n\n"
        f"{ LEXICON_RU['/start']}",
        reply_markup=_create_inline_keyboard(2, btn_help="🆘 Помощь")
    )


@router.message(Command(commands='help'))
async def _help(message: Message):
    await message.answer(
        text=LEXICON_RU['/help'],
        reply_markup=_create_inline_keyboard(2, btn_report="📝 Отчет")
    )


@router.message(Command(commands='report'))
async def _report(message: Message, session: AsyncSession):
    await message.answer(
        text=LEXICON_RU['/report'],
        reply_markup=_create_inline_keyboard(2,
                                             btn_add_report="➕ Добавить",
                                             btn_view_report="🔭 Посмотреть")
    )


@router.callback_query(Text(text=["btn_help"]))
async def _button_help_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/help'],
        reply_markup=_create_inline_keyboard(2, btn_report="📝 Отчет")
    )


@router.callback_query(Text(text=["btn_report"]))
async def _button_report_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['/report'],
        reply_markup=_create_inline_keyboard(2,
                                             btn_add_report="➕ Добавить",
                                             btn_view_report="🔭 Посмотреть")
    )


@router.callback_query(Text(text=["btn_add_report"]))
async def _button_add_reprot_press(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Вы в меню отчетов, введите задачу")
    await state.set_state(AddTask.task)


@router.message(AddTask.task)
async def compeleted_task(message: Message, state: FSMContext):
    await state.update_data(task=message.text)
    logger.debug(message.text)
    # добавление записи в бд
    await message.answer(text="добавлено")


@router.message()
async def _echo(message: Message, current_task: str):
    try:
        logger.debug(current_task)
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
