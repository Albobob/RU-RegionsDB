# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
import database


engine = database.engine

Session = sessionmaker(bind=engine)

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)
