from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base = declarative_base()
metadata = MetaData()