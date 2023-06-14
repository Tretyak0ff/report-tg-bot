import asyncio
from aiogram import Bot, Dispatcher
from loguru import logger
from sqlalchemy.ext.asyncio import async_sessionmaker
from config.loader import Config, load_config, load_engine
from handlers import admin_handlers, user_handlers
from keyboards.set_menu import set_main_menu
from middlewares.database import SessionMiddleware
from aiogram.utils.callback_answer import CallbackAnswerMiddleware


async def main() -> None:
    config: Config = load_config(".env")
    sessionmaker: async_sessionmaker = load_engine(config.database)
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    dp: Dispatcher = Dispatcher()
    dp.update.outer_middleware(SessionMiddleware(session_pool=sessionmaker))
    # dp.callback_query.middleware(CallbackAnswerMiddleware())

    await set_main_menu(bot)
    logger.info('Bot is running')

    # dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
