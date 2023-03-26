from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class GeoCategory(Base):
    __tablename__ = 'geo_category'

    id = Column(Integer, primary_key=True)
    rus_name = Column(String(500))
    eng_name = Column(String(500))

    # rus_total = relationship('RusTotal', backref='geo_category')
    districts = relationship('District', back_populates='geo_category')
    # territorial_unit = relationship('TerritorialUnit', backref='geo_category')

    def __repr__(self):
        return f"<GeoCategory(id={self.id}, name={self.name}, name_eng={self.name_eng})>"
