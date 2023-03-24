from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

# Создаем соединение с базой данных
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Создаем экземпляр класса, который будет использован для определения таблиц в базе данных
Base.metadata.create_all(engine)