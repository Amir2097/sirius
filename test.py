from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fake_useragent import UserAgent
from dotenv import load_dotenv
import sqlalchemy as sq
from typing import Type
import datetime
import requests
import json
import os

ua = UserAgent()
load_dotenv()
Base = declarative_base()


class Quiz(Base):

    __tablename__ = "quiz"

    id = sq.Column(sq.Integer, primary_key=True)
    id_quiz = sq.Column(sq.Integer)
    answer = sq.Column(sq.String(60))
    question = sq.Column(sq.String)
    value = sq.Column(sq.Integer)
    airdate = sq.Column(sq.DateTime)
    created_at = sq.Column(sq.DateTime)
    updated_at = sq.Column(sq.DateTime)
    category_id = sq.Column(sq.Integer)
    game_id = sq.Column(sq.Integer)
    invalid_count = sq.Column(sq.String)
    category = sq.Column(sq.String)

    def __str__(self):
        return f'Quiz: {self.id_quiz}, {self.answer}, {self.category}!'

    @property
    def as_dict(self):
        """
        RU: Сериализация полученных данных из БД
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def create_tables(engine):
    """
    RU: Создание и удаление моделей из БД
    :param engine: create_engine(DSN)
    """
    # Base.metadata.drop_all(engine) # delete models
    Base.metadata.create_all(engine)  # create models


ORM_MODEL_CLS = Type[Quiz] # Type models

DSN = f'postgresql+psycopg2://{os.getenv("DATABASE_USER")}:{os.getenv("DATABASE_PASSWORD")}' \
      f'@{os.getenv("DATABASE_HOST")}:{os.getenv("DATABASE_PORT")}/{os.getenv("DATABASE_NAME")}' # Соединение с БД

engine = sq.create_engine(DSN)
# create_tables(engine) # Create models in DB

Session = sessionmaker(bind=engine)
session = Session()


# ----------------class Test-------------
class Test:
    """
    Ru: Класс для работы с API https://jservice.io/
    """

    def __init__(self, x: int, y: int):
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
        else:
            raise TypeError(f'Invalid data type of the argument')

    def get_quiz(self):
        """
        RU: Метод который получвет x викторин и записывает в бд с проверкой на уникальность
        """
        url = f'https://jservice.io/api/random?count={self.x}'
        response = requests.get(url=url, headers={'user-agent': f'{ua.random}'})

        if response.status_code != 200:
            raise Exception(f'Check response status code: {response.status_code}')

        data = response.json()
        for simple in data:
            user_verification = session.query(Quiz.id).filter(Quiz.id_quiz == simple['id'])
            if session.query(user_verification.exists()).scalar():
                pass
            else:
                new_data = Quiz(
                    id_quiz=simple['id'], answer=simple['answer'], question=simple['question'], value=simple['value'],
                    airdate=simple['airdate'], created_at=simple['created_at'], updated_at=simple['updated_at'],
                    category_id=simple['category_id'], game_id=simple['game_id'],
                    invalid_count=simple['invalid_count'], category=simple['category']['title']
                )
                session.add(new_data)
                session.commit()
        return f'New quiz added!'

    def get_category(self, category: str):
        """
        RU: Метод получения кол-ва записей в категории
        :param category:  название категории викторин
        """
        count_category = session.query(Quiz.id).filter(Quiz.category == category).count()
        return f'Category: {category}, {count_category} entries.'

    def json_entries(self):
        """
        RU: Метод возвращает y(указали при инициализации) записей с бд,
        записывает в json c названием текущей даты запроса данных
        """
        limit_entries = [x.as_dict for x in session.query(Quiz).limit(self.y).all()]
        simple = [{
            f'{datetime.datetime.now()}': limit_entries
        }]
        with open(f'Entries {self.y}.json', 'w') as file:
            file.write(json.dumps(simple, ensure_ascii=False, indent=4, default=str))

        return f'Complete'

