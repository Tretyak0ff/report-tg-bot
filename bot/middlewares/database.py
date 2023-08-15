from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery
from sqlalchemy.ext.asyncio import async_sessionmaker
from models.user import _get_user
from loguru import logger
from datetime import datetime, timedelta, timezone


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
        # logger.error(data.get("event_from_user"))
        async with self.session() as session:
            data["session"] = session
            data["user"] = await _get_user(
                aiogram_user=data.get("event_from_user"),
                session=session)
            return await handler(event, data)


class CallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        message_date = event.message.date
        now_date = datetime.utcnow().replace(tzinfo=timezone.utc)
        delta_date = timedelta(seconds=10)
        if message_date < now_date - delta_date:
            await event.answer(
                text="Кнопка устарела!\n Повторите команду",
                show_alert=True
            )
        else:
            return
