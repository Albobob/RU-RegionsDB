from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///ticks.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class RusTotal(Base):
    __tablename__ = 'rus_total'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)  # наименование округа на русском языке
    name_eng = Column(String(500))  # наименование округа на английском языке
    name_transliteration = Column(String(500))  # наименование округа транслитом (так в конституции РФ)


class District(Base):
    __tablename__ = 'district'
    # Округа

    id = Column(Integer, primary_key=True)  # уникальный идентификатор округа
    rus_total_id = Column(Integer, ForeignKey('rus_total.id'))

    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500))
    name_transliteration = Column(String(500))

    objects_class = Column(Integer, nullable=False)


class ClassificationObjects(Base):
    __tablename__ = 'objects_class'

    id = Column(Integer, primary_key=True)
    name = Column(String(500))


Base.metadata.create_all(engine)
