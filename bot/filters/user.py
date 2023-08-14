from typing import Union, Dict, Any
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import _get_user
from models.database import User


class FilterUser(BaseFilter):
    async def __call__(self, callback: CallbackQuery,
                       session: AsyncSession) -> Union[bool, Dict[str, Any]]:
        user: User = await _get_user(aiogram_user=callback.from_user,
                                     session=session)
        return {"user": user}
