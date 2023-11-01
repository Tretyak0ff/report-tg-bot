import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from loguru import logger
from sqlalchemy.ext.asyncio import async_sessionmaker
from config.loader import Config, load_config
from handlers import handler_user
from callbacks import callback_user
from callbacks import callback_user_profile, callback_user_report
from keyboards.set_menu import set_main_menu
from middlewares.user import SessionMiddleware
from aiogram.utils.callback_answer import CallbackAnswerMiddleware


async def main() -> None:
    config: Config = load_config(".env")
    async_session: async_sessionmaker = config.get_session()
    storage: MemoryStorage = MemoryStorage()
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

    dp: Dispatcher = Dispatcher(storage=storage)
    dp.update.outer_middleware(SessionMiddleware(session=async_session))
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    await set_main_menu(bot)
    logger.info('Bot is running')

    dp.include_router(handler_user.router)
    dp.include_router(callback_user.router)

    dp.include_router(callback_user_report.router)
    dp.include_router(callback_user_profile.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
