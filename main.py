from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///ticks.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Rus_total(Base):
    __table_name__ = 'Rus_total'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)  # наименование округа на русском языке
    name_eng = Column(String(500), )  # наименование округа на английском языке
    name_transliteration = Column(String(500))  # наименование округа транслитом (так в конституции РФ)


class District(Base):
    __table_name__ = 'District'
    # Округа

    id = Column(Integer, primary_key=True)  # уникальный идентификатор округа
    rus_total_id = Column(Integer, ForeignKey('Rus_total'))

    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500), )
    name_transliteration = Column(String(500))

    objects_class = Column(Integer, nullable=False)


class Classification_objects(Base):
    __table_name__ = 'Objects_class'

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
