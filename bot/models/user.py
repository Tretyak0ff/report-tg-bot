from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types.user import User as AiogramUser
from models.database import User, Task
from datetime import datetime


async def _create_user(aiogram_user: AiogramUser) -> User:
    new_user = User(telegram_user_id=aiogram_user.id,
                    created_at=datetime.now(),
                    first_name=aiogram_user.first_name,
                    last_name=aiogram_user.last_name,
                    username=aiogram_user.username,
                    work_mode=None)
    return new_user


async def _update_user(user: User, aiogram_user: AiogramUser) -> User:
    update_user = User(id=user.id,
                       telegram_user_id=user.telegram_user_id,
                       created_at=user.created_at,
                       first_name=aiogram_user.first_name,
                       last_name=aiogram_user.last_name,
                       username=aiogram_user.username,
                       work_mode=user.work_mode)
    return update_user


async def _get_user(aiogram_user: AiogramUser,
                    session: AsyncSession) -> User:
    user = await(session.scalar(select(User).where(id == id)))
    if user:
        user = await _update_user(user=user, aiogram_user=aiogram_user)
        await session.merge(user)
    else:
        user = await _create_user(aiogram_user=aiogram_user)
        session.add(user)
    await session.close()
    return user


async def _create_task(user: User, task: str, session: AsyncSession) -> Task:
    new_task = Task(
        task=task,
        created_at=datetime.now(),
        user_id=user.id
    )
    session.add(new_task)
    await session.commit()
    return new_task
