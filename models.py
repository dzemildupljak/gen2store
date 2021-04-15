from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base


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
    __tablename__ = "customer's data"
    id = Column("id", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    telephone_number = Column("telephone_number", String)
    points = Column("Points", Integer)
    bill = relationship("Bill")


class Bill(Base):
    __tablename__ = "Bill"
    id = Column("id", Integer, primary_key=True)
    bill_number = Column('bill_number', String)
    bill_date = Column('bill_date', DateTime)
    customer_id = Column('customer_id', Integer, ForeignKey("customer.id"))
