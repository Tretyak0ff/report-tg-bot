import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger
from sqlalchemy.ext.asyncio import async_sessionmaker
from config.loader import Config, load_config, load_engine
from handlers import user_handlers
from callbacks import user_callbacks
from callbacks import user_callbacks_profile, user_callbacks_report
from keyboards.set_menu import set_main_menu
from middlewares.user import SessionMiddleware
from aiogram.utils.callback_answer import CallbackAnswerMiddleware


async def main() -> None:
    config: Config = load_config(".env")
    async_session: async_sessionmaker = load_engine(config.database)
    storage: MemoryStorage = MemoryStorage()
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    dp: Dispatcher = Dispatcher(storage=storage)
    dp.update.outer_middleware(SessionMiddleware(session=async_session))
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    await set_main_menu(bot)
    logger.info('Bot is running')

    # dp.include_router(admin_handlers.router)
    # @router.callback_query(Checks.user)

    dp.include_router(user_handlers.router)
    dp.include_router(user_callbacks.router)

    dp.include_router(user_callbacks_report.router)
    dp.include_router(user_callbacks_profile.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
