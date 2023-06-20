from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def _create_inline_keyboard(width: int,
                            last_btn: str | None = None,
                            **kwargs: str) -> InlineKeyboardMarkup:
    keyboard_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))
    keyboard_builder.row(*buttons, width=width)
    if last_btn:
        keyboard_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data="last_btn"
        ))
    return keyboard_builder.as_markup()
