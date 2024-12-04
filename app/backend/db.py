from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# Движок SQLAlchemy, который управляет соединениями с базой
engine = create_engine("sqlite:///taskmanager.db", echo=True)

# Фабрика для создания сессий, необходимых для запросов к базе данных
SessionLocal = sessionmaker(bind=engine)


# Базовый класс для моделей SQLAlchemy. Все модели будут наследоваться от него
class Base(DeclarativeBase):
    pass
