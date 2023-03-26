# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.geo_category import GeoCategory
from models.rus_total import RusTotal
from models.district import District
from models.territorial_unit import TerritorialUnit

engine = create_engine("sqlite:///database.db", echo=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

