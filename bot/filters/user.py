from typing import Union, Dict, Any
from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from services.database import _get_or_create_user


class WorkMode(BaseFilter):
    async def __call__(self, callback: CallbackQuery,
                       session: AsyncSession) -> Union[bool, Dict[str, Any]]:
        user = await _get_or_create_user(aiogram_user=callback.from_user,
                                         session=session)
        if user.work_mode:
            return {"user": user}


class AbsenceWorkMode(BaseFilter):
    async def __call__(self, callback: CallbackQuery,
                       session: AsyncSession) -> Union[bool, Dict[str, Any]]:
        user = await _get_or_create_user(aiogram_user=callback.from_user,
                                         session=session)
        return {"user": user}
