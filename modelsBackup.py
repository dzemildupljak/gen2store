import datetime
import uuid
from sqlalchemy import create_engine, Column, Integer, String
from database import Base


class Shop(Base):
    __tablename__ = 'shops'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    type = Column('type', String)

    def __init__(self):
        self.id = None
        self.name = None
        self.type = None


class Product:
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    type = Column('type', String)
    price = Column('price', Integer)
    serial_number = Column('serial_number', String)
    supplies = Column('supplies', Integer)

    def __init__(self, id, name, typ, price, serialnumber):
        self.id = id
        self.name = name
        self.type = typ
        self.price = price
        self.serial_number = serialnumber


# class User(Base):
#     __tablename__ = 'users'
#     id = Column('id', Integer, primary_key=True)
#     ime = Column('ime', String)
#     prezime = Column('prezime', String)
#     username = Column('username', String, unique=True)
#     password = Column('password', String)
#     schoolId = Column('schoolId', Integer)

#     def __init__(self):
#         self.ime = None
#         self.prezime = None
#         self.username = None
#         self.password = None
#         self.schoolId = None


# class Customer:
#     def __init__(self):
#         self.first_name = None
#         self.last_name = None
#         self.telephone_number = None


#     # def __init__(self):
#     #     self.id = None
#     #     self.name = None
#     #     self.type = None
#     #     self.price = None
#     #     self.quantite = None
#     #     self.serial_number = None

#     # def create_product_data(self):
#     #     self.id = uuid.uuid1()
#     #     self.name = input('Unesite ime proizvoda: ')
#     #     self.type = input('Unesite tip proizvoda: ')
#     #     self.price = float(input('Cena proivda: '))
#     #     supplies = float(input('Kolicina proizvoda'))
#     #     if self.type in ('medicine', 'parking ticket'):
#     #         self.serial_number = input('Serijski broj: ')

#     # def sell_product(self, shopType):

#     #     if shopType == 'corner shop' and self.type == 'cigarettes':
#     #         if self.supplies >= self.quantite:
#     #             self.supplies -= self.quantite
#     #         else:
#     #             print('Nemamo dovoljno na zalihama!!!')
#     #     elif shopType == 'pharmacies' and self.type == 'medicine':
#     #         if self.supplies >= self.quantite:
#     #             self.supplies -= self.quantite
#     #         else:
#     #             print('Nemamo dovoljno na zalihama!!!')
#     #     else:
#     #         if self.supplies >= self.quantite:
#     #             self.supplies -= self.quantite
#     #         else:
#     #             print('Nemamo dovoljno na zalihama!!!')


# class Bill:
#     def __init__(self):
#         self.id = None
#         self.number_of_bill = '00000'
#         self.date_of_bill = None
#         self.customer_data = None
#         self.product_list = []


# # Base.metadata.create_all(bind=engine)
