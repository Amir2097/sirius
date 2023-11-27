# Небольшвя реализация API взаимодействия
_Django (DRF)_

**Ендпоинты**:

- api/imagelist/ - получение списка картинок и писанием (GET)
- api/image/post/ - добавление новой картинки в формате Base64 и описанием (POST)
- api/image/delete/<int:pk>/ - удаление картинки по ID (DELETE)

## Использованные технологии:

1. Python 3.11
2. Django (DRF)
3. БД:
   - PostgreSQL
4. Хранение переменных окружения:
   - Python-dotenv

> Установите библиотеки:
- `pip install -r requirements.txt`

*Переменные окружения:*
- Библиотека *python-dotenv*. Очень удобная и практичная в использовании.

  1. Создайте файл `.env` и внесите ваши данные 
  2. Переменные:
      - `SECRET_KEY`
      - `DATABASE_NAME`
      - `DATABASE_PORT`
      - `DATABASE_USER`
      - `DATABASE_PASSWORD`
      - `DATABASE_HOST`
      - `DATABASE_ENGINE`

## Для запуска проекта и проверки ендпоинтов:

- Проведите создание и применение миграций 
   - `python manage.py makemigrations`
   - `python manage.py migrate`
- Запуск django проекта:
   - `python manage.py runserver` либо `./manage.py runserver`


---

# Test.py

**Взаимодействие с API https://jservice.io/**

## Использованные технологии:

1. Python 3.11
2. БД:
   - PostgreSQL
   - Модель на основе SQLalchemy
   - Psycopg2
3. Хранение переменных окружения:
   - Python-dotenv
4. Библиотека fake_useragent
   - Современный простой фейкер пользовательского агента с реальной базой данныx

> Установите библиотеки:
- `pip install -r requirements.txt`

## Class Test

- Инициализация `__init__` - принимает  2 именованных аргумента x, y.  Должны быть числами, 
реализована проверка.
- Метод **get_quiz** - получать x викторин с https://jservice.io/ и записывает в бд с проверкой на уникальность. 
Записи разложены по категориям.
- Метод **get_category** - получает кол-во записей в категории. В качестве аргумента принимает название категории.
- Метод **json_entries** - возвращает y записей с БД и сохраняет в json c названием текущей даты запроса данных.







      
