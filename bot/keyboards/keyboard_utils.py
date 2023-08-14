from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loguru import logger
from aiogram.filters.callback_data import CallbackData


class UserCallback(CallbackData, prefix="work_mode"):
    action: str
    value: str


def _create_inline_keyboard(width: int,
                            *args: str,
                            last_btn: str | None = None,
                            **kwargs: str
                            ) -> InlineKeyboardMarkup:
    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    if args:
        for button in args:
            keyboard_builder.button(
                text=button['text'], callback_data=UserCallback(
                    action=button['action'], value=button['value']))
            keyboard_builder.adjust(width)
    if kwargs:
        for button, text in kwargs.items():
            keyboard_builder.button(
                text=text,
                callback_data=button)
            keyboard_builder.adjust(width)
    if last_btn:
        keyboard_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data="last_btn"
        ))
    return keyboard_builder.as_markup()
