from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class TerritorialUnit(Base):
    __tablename__ = 'territorial_unit'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500))
    district_id = Column(Integer, ForeignKey('districts.id'), nullable=False)
    geo_category_id = Column(Integer, ForeignKey('geo_category.id'), nullable=False)

    district = relationship('District', backref='territorial_unit')
    geo_category = relationship('GeoCategory', backref='territorial_units')

