from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import LEXICON_RU
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from services.user import _get_or_create_user
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
    user = await _get_or_create_user(
        aiogram_user=message.from_user, session=session)
    logger.debug(user.__dict__)

    # await message.answer(
    #     text=LEXICON_RU['/report'],
    #     reply_markup=_create_inline_keyboard(
    #         2,
    #         btn_add_report="➕ Добавить",
    #         btn_view_report="🔭 Посмотреть")
    # )
    # logger.debug(await _get_or_create_user(message=message, session=session))


@router.message(AddTask.task)
async def compeleted_task(message: Message, state: FSMContext,
                          session: AsyncSession):
    await state.update_data(task=message.text)
    # logger.debug(await state.get_data())

    # добавление записи в бд

    await message.answer(
        text=LEXICON_RU['/add_task'],
        reply_markup=_create_inline_keyboard(
            2,
            btn_compelete_report="✅ Завершить")
    )


@router.message()
async def _echo(message: Message, current_task: str):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
