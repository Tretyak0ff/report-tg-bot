from aiogram.filters.state import State, StatesGroup


class AddTask(StatesGroup):
    task = State()
