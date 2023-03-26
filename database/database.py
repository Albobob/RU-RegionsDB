from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.base import Base, SQLALCHEMY_DATABASE_URI
# from models.district import District

# создание соединения с базой данных

engine = create_engine(SQLALCHEMY_DATABASE_URI)

# создание таблиц в базе данных
Base.metadata.create_all(engine)
