from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class RusTotal(Base):
    __tablename__ = 'rus_total'

    id = Column(Integer, primary_key=True)
    name_ru = Column(String(500), nullable=False)
    name_eng = Column(String(500))
    geo_category_id = Column(Integer, ForeignKey('geo_category.id'), nullable=False)
    districts = relationship('District', backref='rus_total')

    def __repr__(self):
        return f"<RusTotal(id={self.id}, name_ru='{self.name_ru}', name_eng='{self.name_eng}', " \
               f"short_name_ru='{self.short_name_ru}', short_name_eng='{self.short_name_eng}')>"
