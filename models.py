from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base


class Shop(Base):
    __tablename__ = 'shops'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    typee = Column('type', String)
    city = Column("city", String)
    zipp = Column("zip", String)
    address = Column("adresa", String)
    products = relationship('Product', backref='shop')


class Product(Base):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    typee = Column('type', String)
    price = Column('price', String)
    quantity = Column('quantity', String)
    serial_number = Column('serial number', String)
    shop_id = Column('shop_id', Integer, ForeignKey('shops.id'))


class Customer(Base):
    __tablename__ = "customers"
    id = Column("id", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    telephone_number = Column("telephone_number", String)
    points = Column("Points", Integer)
    bill = relationship("Bill")


class Bill(Base):
    __tablename__ = "bills"
    id = Column("id", Integer, primary_key=True)
    bill_number = Column('bill_number', String)
    bill_date = Column('bill_date', DateTime)
    customer_id = Column('customer_id', Integer, ForeignKey("customers.id"))


class Cart(Base):
    __tablename__ = "cart"
    id = Column("id", Integer, primary_key=True)
    price = Column("price", Float)
