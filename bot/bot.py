import asyncio
from aiogram import Bot, Dispatcher
from loguru import logger
from peewee import Database
from peewee_async import PostgresqlDatabase

from config.loader import Config, load_config
from handlers import admin_handlers, user_handlers
from keyboards.set_menu import set_main_menu
from middlewares.database import SessionMiddleware


async def main() -> None:
    config: Config = load_config(".env")
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    db: Database = PostgresqlDatabase(
        config.database.name,
        host=config.database.host,
        port=config.database.port,
        user=config.database.user,
        password=config.database.password
    )

    dp: Dispatcher = Dispatcher()
    dp.update.outer_middleware(SessionMiddleware(database=db))

    await set_main_menu(bot)
    logger.info('Bot is running')

    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
