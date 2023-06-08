from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from loguru import logger
from peewee import Database


class SessionMiddleware(BaseMiddleware):
    def __init__(self, database: Database) -> None:
        logger.info(database)
        self.database = database
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        # async with self.database() as database:
        # data["database"] = self.database()
        logger.debug(event)
        logger.info(data)
        # return await handler(event, data)

        # print("Before handler")
        # result = await handler(event, data)
        # print("After handler")
        # return result


class AdminMiddleware(BaseMiddleware):
    pass
