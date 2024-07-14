from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    image_url = Column(String)
