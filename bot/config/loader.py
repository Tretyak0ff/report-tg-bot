from dataclasses import dataclass
from environs import Env


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
