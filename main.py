# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from alembic import op

engine = create_engine("sqlite:///ticks.db", echo=True, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class GeoCategory(Base):
    __tablename__ = 'geo_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    name_eng = Column(String(500))
    rus_total = relationship('RusTotal', backref='geo_category')


class RusTotal(Base):
    __tablename__ = 'rus_total'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500))
    geo_category_id = Column(Integer, ForeignKey('geo_category.id'), nullable=False)
    districts = relationship('District', backref='rus_total')


class District(Base):
    __tablename__ = 'districts'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500))
    short_name_ru = Column(String(8))
    short_name_eng = Column(String(10))
    rus_total_id = Column(Integer, ForeignKey('rus_total.id'), nullable=False)
    geo_category_id = Column(Integer, ForeignKey('geo_category.id'), nullable=False)

    rus_total = relationship('RusTotal', backref='districts')
    geo_category = relationship('GeoCategory', backref='districts')


class TerritorialUnit(Base):
    __tablename__ = 'territorial_unit'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500))
    district_id = Column(Integer, ForeignKey('districts.id'), nullable=False)
    geo_category_id = Column(Integer, ForeignKey('geo_category.id'), nullable=False)

    district = relationship('District', backref='territorial_unit')
    geo_category = relationship('GeoCategory', backref='territorial_units')


Base.metadata.create_all(engine)

