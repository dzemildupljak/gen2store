from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
import datetime


class Shop(Base):
    __tablename__ = 'shops'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    type = Column('type', String)
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
    __tablename__ = 'customers'
    id = Column('id',Integer,primary_key=True)
    first_name = Column('first name',String)
    last_name = Column('last name',String)
    telephone_number = Column('telephone number',String)

class Bill(Base):
    __tablename__ = 'bills'
    id = Column('id',Integer,primary_key=True)
    date_of_bill = Column('date',datetime)
    customer_id = Column('customer_id', Integer, ForeignKey('customers.id'))
