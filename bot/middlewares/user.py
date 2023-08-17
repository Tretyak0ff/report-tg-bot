from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery
from sqlalchemy.ext.asyncio import async_sessionmaker
from models.user import _get_user
from loguru import logger
from datetime import datetime, timedelta, timezone
from aiogram.methods import EditMessageText, DeleteMessage, EditMessageReplyMarkup


class SessionMiddleware(BaseMiddleware):
    def __init__(self, session: async_sessionmaker) -> None:
        super().__init__()
        self.session = session

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        async with self.session() as session:
            data["session"] = session
            data["user"] = await _get_user(
                aiogram_user=data.get("event_from_user"),
                session=session)
            return await handler(event, data)


class MessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        try:
            await EditMessageReplyMarkup(chat_id=event.chat.id,
                                         message_id=event.message_id-1)
        finally:
            return await handler(event, data)


class CallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        try:
            await EditMessageReplyMarkup(chat_id=event.message.chat.id,
                                         message_id=event.message.message_id)
        finally:

            # logger.error(event.message.message_id)
            # logger.error(event.message.chat.id)
            # logger.error(event.message.message_id)
            # # logger.error(event.chat)
            # # logger.error(event.message.chat.id)
            message_date = event.message.date
            now_date = datetime.utcnow().replace(tzinfo=timezone.utc)
            delta_date = timedelta(minutes=5)

            if message_date < now_date - delta_date:
                await event.answer(
                    text="Кнопка устарела!\n\n Повторите команду",
                    show_alert=True
                )
            else:
                return await handler(event, data)
