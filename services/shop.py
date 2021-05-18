from helpers import convert_to_dict
from database import SessionLocal
import models

db = SessionLocal()


def add_new_shop():
    s1 = models.Shop()
    s1.name = input('Unesite ime shop-a: ')
    while s1.typee not in ('supermarket', 'cornershop', 'pharmacy'):
        s1.typee = input('Unesite tip shop-a: ')
    try:
        db.add(s1)
        db.commit()
        db.refresh(s1)
        db.close()
        return s1
    except:
        print('Doslo je do greske pri upisivanju u bazi')
        return False


def get_all():
    shops = db.query(models.Shop).all()
    if not shops:
        return False
    return shops


def get_by_id(id):
    shop = db.query(models.Shop).filter(models.Shop.id == id).first()
    if not shop:
        return False
    return shop


def get_by_city_shop(city):
    shops = db.query(models.Shop).filter(models.Shop.city == city).all()
    if not shops:
        return False
    return shops


def get_by_address_shop(address):
    shops = db.query(models.Shop).filter(models.Shop.address == address).all()
    if not shops:
        return False
    return shops


def delete(id):
    shops = db.query(models.Shop).filter(models.Shop.id == id)

    if not shops.first:
        return False

    shops.delete()
    db.commit()
    return True


def update(id, newShop):
    shops = db.query(models.Shop).filter(models.Shop.id == id)

    if not shops.first():
        return False

    shops.update(convert_to_dict(newShop), synchronize_session=False)
    db.commit()
    return True
