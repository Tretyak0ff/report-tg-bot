from sqlalchemy import Column, BigInteger, DateTime, String, Boolean
from models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    telegram_user_id = Column(BigInteger)
    created_at = Column(DateTime())
    first_name = Column(String(), nullable=True)
    last_name = Column(String(), nullable=True)
    username = Column(String(), nullable=True)
    is_admin = Column(Boolean(), default=False)
