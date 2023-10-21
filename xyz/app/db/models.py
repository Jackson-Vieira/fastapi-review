from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from app.db.base import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    slug = Column("slug", String, nullable=False)

    products = relationship('Product', back_populates="category")

class Product(Base):
    __tablename__ = "product"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    slug = Column("slug", String, nullable=False)
    price = Column("price", Float, nullable=False)
    stock = Column("stock", Integer, default=0)
    created_at = Column("created_at", DateTime, server_default=func.now())
    created_at = Column("updated_at", DateTime, onupdate=func.now())

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")