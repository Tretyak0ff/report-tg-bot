from sqlalchemy import Column, BigInteger, DateTime, String, Boolean
from sqlalchemy import ForeignKey
from models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    telegram_user_id = Column(BigInteger)
    created_at = Column(DateTime(timezone=True))
    first_name = Column(String(), nullable=True)
    last_name = Column(String(), nullable=True)
    username = Column(String(), nullable=True)
    is_superuser = Column(Boolean(), default=False)
    work_mode = Column(String(), nullable=True)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=True)
    task = Column(String(), nullable=True)
    created_at = Column(DateTime(timezone=True))

    user_id = Column(BigInteger, ForeignKey('users.id'))
