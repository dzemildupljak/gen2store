from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from database import Base


class Shop(Base):
    __tablename__ = 'shops'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    typee = Column('type', String)
    products = relationship('Product', backref='shop')


class Product(Base):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    typee = Column('type', String)
    price = Column('price', String)
    serial_number = Column('serial number', String)
    shop_id = Column('shop_id', Integer, ForeignKey('shops.id'))
    storage = relationship("Storage", uselist=False, back_populates="product")


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
    # TODO dodati listu artikala za bill


cart_product_table = Table('cart_product_table', Base.metadata,
                           Column('cart_id', Integer, ForeignKey('carts.id')),
                           Column('product_id', Integer, ForeignKey('products.id')))


class Cart(Base):
    __tablename__ = 'carts'
    id = Column('id', Integer, primary_key=True)
    shop_id = Column('shop_id', Integer, ForeignKey('shops.id'))
    customer_id = Column('customer_id', Integer, ForeignKey('customers.id'))
    products = relationship("Product",
                            secondary=cart_product_table)
    price = Column('price', String)


class Storage(Base):
    __tablename__ = "storage"
    id = Column('id', Integer, primary_key=True)
    product_id = Column('product_id', Integer, ForeignKey('products.id'))
    product = relationship("Product", back_populates="storage")
    quantity = Column('quantity', Integer)


class SellProducts


(Base):
    __tablename__ = "sell_products"
    id = Column('id', Integer, primary_key=True)
    product_id = Column('product_id', Integer, ForeignKey('products.id'))
    product = relationship("Product")
    quantity = Column('quantity', Integer)
    price = Column('price', Integer)
    bill_id = Column('bill.id', Integer, ForeignKey('bills.id'))
    bill = relationship("Bill")
