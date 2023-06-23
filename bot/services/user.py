# from loguru import logger
# from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types.user import User as AiogramUser
from models.user import User
from datetime import datetime


async def _get_user(id: int, session: AsyncSession) -> User:
    user = await(session.scalar(select(User).where(id == id)))
    return user


async def _create_user(aiogram_user: AiogramUser,
                       session: AsyncSession) -> User:
    new_user = session.add(
        User(telegram_user_id=aiogram_user.id,
             created_at=datetime.now(),
             first_name=aiogram_user.first_name,
             last_name=aiogram_user.last_name,
             username=aiogram_user.username,
             work_mode=None)
    )
    await session.commit()
    return new_user


async def _update_user(user: User,
                       aiogram_user: AiogramUser,
                       session: AsyncSession) -> User:
    update_user = await session.merge(
        User(id=user.id,
             telegram_user_id=user.telegram_user_id,
             created_at=user.created_at,
             first_name=aiogram_user.first_name,
             last_name=aiogram_user.last_name,
             username=aiogram_user.username,
             work_mode=user.work_mode)
    )
    await session.commit()
    return update_user


async def _get_or_create_user(aiogram_user: AiogramUser,
                              session: AsyncSession) -> User:
    user = await _get_user(id=aiogram_user.id, session=session)
    if user is None:
        await _create_user(aiogram_user=aiogram_user,
                           session=session)
        user = await _get_user(id=aiogram_user.id, session=session)
    else:
        user = await _update_user(user=user,
                                  aiogram_user=aiogram_user,
                                  session=session)
    return user

    # logger.error(user)
    # return user

    # if user is None:

    #     # user = update_user(user, name, username)

    #     # return user
    #     logger.debug("user None")

    # return user
    # return create_user(id, name, username, language)
