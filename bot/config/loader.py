from dataclasses import dataclass
from environs import Env
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


@dataclass
class TGBot:
    token: str
    admins_id: list[int]


@dataclass
class DBConfig:
    name: str
    host: str
    port: int
    user: str
    password: str


@dataclass
class Config:
    tg_bot: TGBot
    database: DBConfig


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)
    cnfg = Config(tg_bot=TGBot(token=env("BOT_TOKEN"),
                               admins_id=list(map(int, env.list("ADMINS")))
                               ),
                  database=DBConfig(name=env("DB_NAME"),
                                    host=env("DB_HOST"),
                                    port=env("DB_PORT"),
                                    user=env("DB_USER"),
                                    password=env("DB_PASSWORD")
                                    )
                  )
    return cnfg


def get_url_database(database: Config) -> str:
    return (f"postgresql+asyncpg://{database.user}:"
            f"{database.password}@{database.host}:"
            f"{database.port}/{database.name}")


def load_engine(database: Config) -> async_sessionmaker:
    engine = create_async_engine(
        url=get_url_database(database=database), echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    return sessionmaker
