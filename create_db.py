# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.geo_category import GeoCategory
from models.rus_total import RusTotal
from models.district import District
from models.territorial_unit import TerritorialUnit

engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

categories = [('Страна', 'Country'),
              ('Округ', 'District'),
              ('Республика', 'Republic'),
              ('Край', 'Territories'),
              ('Автономный округ', 'Autonomous Area '),
              ('Область', 'Region'),
              ('Автономная область', 'Autonomous Region'),
              ('Город федерального значения', 'City'),
              ]


for category in categories:
    gc = GeoCategory(rus_name=category[0], eng_name=category[1])
    session.add(gc)

districts = [('Центральный федеральный округ', 'Central Federal District', 'ЦФО', 'CFD'),
             ('Северо-Западный федеральный округ', 'Northwestern Federal District', 'СЗФО', 'NW-FD'),
             ('Южный федеральный округ', 'Southern Federal District', 'ЮФО', 'SFD'),
             ('Северо-Кавказский федеральный округ', 'North Caucasus Federal District', 'СКФО', 'NCD'),
             ('Приволжский федеральный округ', 'Privolzhsky Federal District', 'ПФО', 'PFD'),
             ('Уральский федеральный округ', 'Urals Federal District', 'УФО', 'UFD'),
             ('Сибирский федеральный округ', 'Siberian Federal District', 'СФО', 'SFD'),
             ('Дальневосточный федеральный округ', 'Fareast Federal District', 'ДФО', 'FED')]





session.commit()
session.close()