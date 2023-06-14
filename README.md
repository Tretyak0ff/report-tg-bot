report-tg-bot
---
Бот формирует отчеты по форме на основе присланных пользователями данных. 
Создано для ООО «Газпром СПГ Портовая»
---
### 📝 *.env*

*Файл с секретами, которые загружаются в переменные окружения. Не забыть добавить его в .gitignore.*

### 📝 *.env.example*

*Пример файла с секретами. Нужно не забывать его обновлять, при изменениях структуры реального .env-файла.*

###  📝 *.gitignore*

*Файл для системы контроля версий, в котором прописаны файлы и директории проекта, которые не следует отслеживать.*

### 📝 *tg_bot.py*

*Основной файл проекта - точка входа в проект.  pyproject.tomlФайл с зависимостями - версиями библиотек, используемыми в проекте.*

### 📁 *.config_data/*
*Пакет для хранения файлов с конфигурационными данными.*
- 📝 config.py
> Файл с конфигурационными данными для бота, базы данных, сторонних сервисов и т.п.

### 📁 *.errors/*
Пакет с модулями для обработки исключений, возникающих в процессе работы бота.
- 📝 errors.py
> Модуль с обработчиками исключений.

### 📁 *.external_services/*
Пакет с модулями для работы с API внешних сервисов.

### 📁 *.filters/*
*Пакет с кастомными фильтрами, если не хватает встроенных фильтров самого aiogram, или если анонимная функция, при регистрации хэндлеров в диспетчере, получается слишком громоздкой и ее лучше убрать из регистратора.*
- 📝 is_admin.py
> Модуль с функцией-фильтром, проверяющей пользователя, является ли он администратором бота. 
- 📝 language_filter.py
> Языковой фильтр. Актуален для мультиязычных ботов. Если бот работает только на одном языке - такой фильтр не требуется.

### 📁 *.handlers/*
*Пакет, в котором хранятся обработчики апдейтов.*
- 📝 admin_handlers.py
> Модуль с хэндлерами, срабатывающими на действия пользователя, если он является администратором бота.
- 📝 private_user_handlers.py
> Модуль с хэндлерами, срабатывающими на действия пользователей с каким-то другим статусом, например, если они заплатили за дополнительный функционал бота.
- 📝 user_handlers.py
> Модуль с хэндлерами для пользователей с обычным статусом, например, для тех, кто первый раз запустил бота.

### 📁 *.keyboards/*
*Пакет с модулями, в которых хранятся и/или динамически формируются клавиатуры, отправляемые пользователям ботом, в процессе взаимодействия.*
- 📝 keyboard_utils.py
> Вспомогательные функции/методы, помогающие формировать клавиатуры.  
- 📝 set_menu.py
> Модуль для установки команд в нативную кнопку "Menu" вашего бота.

### 📁 *.lexicon/*
*Пакет для хранения текстов - ответов бота.*
- 📝 lexicon_ru.py
> Модуль со словарем соответствий данных текстам на русском языке.
- 📝 lexicon_en.py
> Модуль со словарем соответствий данных текстам на английском языке.

### 📁 *.middlewares/*
*Пакет, в котором хранятся мидлвари, то есть программы, которые работают с апдейтамм до того момента, как они попадут в хэндлер.*
- 📝 throttling.py
> Модуль с "удушающей миддлварью", то есть с функциями/методами, которые отсекают от хэндлеров апдейты, распознанные как флуд. Например, если пользователь слишком часто жмет одну и ту же кнопку или отправляет много коротких сообщений в короткий промежуток времени.

### 📁 *.models/*
*Пакет с модулями для взаимодействия с базой данных.*
- methods.py
> Модуль с методами для работы с БД.
- 📝 models.py
> Модуль с ORM-моделями базы данных, то есть отображением базы данных в виде объекта с атрибутами, часто совпадающими с полями базы данных. Через такие объекты можно обращаться к базе данных и как-то взаимодействовать с ней, обращаясь к атрибутам и методам объектов.  

### 📁 *.services/*
*Пакет с модулями для реализации какой-то бизнес-логики бота.*
 - 📝 services.py
 >Соответственно, модуль с реализацией бизнес-логики.  

### 📁 *.states/*
*Пакет с модулями, в которых описаны классы, отражающими возможные состояния пользователей, в процессе взаимодействия с ботом, для реализации машины состояний.*
 - 📝 states.py
 > Соответственно, модуль с классами, отражающими возможные состояния пользователя, в процессе взаимодействия с ботом.  

### 📁 *.tests/*
 *Пакет с тестами для тестирования работы бота перед тем, как развернуть и запустить его в продакшн.*

### 📁 *.utils/*
*Пакет для хранения вспомогательных модулей, которые нужны в процессе работы бота, но по смыслуне попали ни в одну из предыдущих категорий.*
 - 📝 utils.py
 > Модуль с утилитами - вспомогательными скриптами для работы бота.


├── bot
│   ├── alembic.ini
│   ├── bot.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── __pycache__
│   │       ├── config.cpython-310.pyc
│   │       ├── __init__.cpython-310.pyc
│   │       └── loader.cpython-310.pyc
│   ├── handlers
│   │   ├── admin_handlers.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── admin_handlers.cpython-310.pyc
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── sadmin_handlers.cpython-310.pyc
│   │   │   └── user_handlers.cpython-310.pyc
│   │   ├── superuser_handlers.py
│   │   └── user_handlers.py
│   ├── __init__.py
│   ├── keyboards
│   │   ├── __init__.py
│   │   ├── keyboard_utils.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── set_menu.cpython-310.pyc
│   │   └── set_menu.py
│   ├── lexicon
│   │   ├── __init__.py
│   │   ├── lexicon_ru.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-310.pyc
│   │       └── lexicon_ru.cpython-310.pyc
│   ├── middlewares
│   │   ├── database.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── database.cpython-310.pyc
│   │       ├── db.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── migration
│   │   ├── env.py
│   │   ├── __pycache__
│   │   │   └── env.cpython-310.pyc
│   │   ├── README
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 108e8fb1998e_init_users.py
│   │       ├── d47da09e827c_initial.py
│   │       └── __pycache__
│   │           ├── 108e8fb1998e_init_users.cpython-310.pyc
│   │           └── d47da09e827c_initial.cpython-310.pyc
│   ├── models
│   │   ├── base.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── base.cpython-310.pyc
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   └── user.cpython-310.pyc
│   │   └── user.py
│   ├── __pycache__
│   │   ├── bot.cpython-310.pyc
│   │   ├── config.cpython-310.pyc
│   │   └── __init__.cpython-310.pyc
│   └── services
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── users.cpython-310.pyc
│       └── users.py
├── docker-compose.yml
├── poetry.lock
├── pyproject.toml
├── README.md
└── tests
    └── __init__.py


 Используемая литература:
 - SQL Alchemy: 
 https://habr.com/ru/amp/publications/735606/
 - Asyncio telegram bot: 
 https://alexcoder.dev/asynchronous-telegram-bot-with-aiogram-and-gino-orm
 https://stepik.org/lesson/759406/step/2?unit=761422
 - Aiogram3:
 https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/
 https://github.com/MasterGroosha/aiogram-and-sqlalchemy-demo/blob/e4395c5748e2c1102d5d7421e0167a4070a62e16/bot/keyboards.py
 https://github.com/netbriler/aiogram-peewee-template/blob/master/services/users.py