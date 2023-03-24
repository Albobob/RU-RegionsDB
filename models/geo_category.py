from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class GeoCategory(Base):
    __tablename__ = 'geo_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(500))
    name_eng = Column(String(500))
    rus_total = relationship('RusTotal', backref='geo_category')