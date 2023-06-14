from loguru import logger
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import Message
from models.user import User


# def get_user(id: int) -> User:
#     return User.get_or_none(User.id == id)


# def create_user(id: int, name: str, username: str = None, language: str = None) -> User:
#     new_user = User.create(
#         id=id, name=name, username=username, language=language)

#     if id in ADMINS:
#         new_user.is_admin = True
#         new_user.save()

#     logger.info(f'New user {new_user}')

#     return new_user


# def update_user(user: User, name: str, username: str = None) -> User:
#     user.name = name
#     user.username = username
#     user.save()

#     return user


def _get_or_create_user(message: Message, session: AsyncSession) -> User:

    query = select(User).where(User.telegram_user_id ==
                               message.from_user.id)
    user = session.scalar(query)
    return user

    # if user:
    #     user = update_user(user, name, username)

    #     return user

    # return create_user(id, name, username, language)
