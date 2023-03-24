from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


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

    def __repr__(self):
        return f"<District(id={self.id}, name_ru='{self.name_ru}', name_eng='{self.name_eng}', " \
               f"short_name_ru='{self.short_name_ru}', short_name_eng='{self.short_name_eng}', " \
               f"rus_total_id={self.rus_total_id}, geo_category_id={self.geo_category_id})>"

