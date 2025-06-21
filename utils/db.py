from sqlalchemy import (create_engine, Column, Integer,
                        String, BigInteger, Boolean, DateTime, func, ForeignKey)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from data.config import PG_USER, PG_PASS, PG_HOST, PG_PORT, PG_DB

engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class Products(Base):
    __tablename__ = 'products'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    price = Column(BigInteger)

    def save(self, session):
        session.add(self)
        session.commit()
    def delete(self, session , product_id):
        object_to_delete = session.query(Products).filter(Products.id == product_id).first()
        session.delete(object_to_delete)
        session.commit()
    def all_products(self , session):
        products = session.query(Products).all()
        result = ''
        for product in products:
            result += f'Mahsulot nomi-> {product.name} ' + f'mahsulot narxi -> {product.price}\n'
        return result


    def search_product(self, session, name):
        obj = session.query(Products).filter(name == Products.name).first()
        if not obj:
            return False
        return True


    def __repr__(self):
        return f'Products {self.name} , {self.price}>'
