from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class RusTotal(Base):
    __tablename__ = 'rus_total'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500))
    geo_category_id = Column(Integer, ForeignKey('geo_category.id'), nullable=False)
    districts = relationship('District', backref='rus_total')

