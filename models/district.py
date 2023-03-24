from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


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

