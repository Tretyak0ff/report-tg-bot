from models.database import User


def _user(user: User) -> str:
    if user.work_mode == "five-day":
        work_mode = "Пятидневный"
    elif user.work_mode == "shift":
        work_mode = "Сменный"
    else:
        work_mode = "Не определен"

    return (f"Имя: {user.first_name}\n"
            f"Фамилия: {user.last_name}\n"
            f"Ник: {user.username}\n"
            f"Режим работы: {work_mode}\n\n")
