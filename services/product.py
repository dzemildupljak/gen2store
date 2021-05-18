from sqlalchemy.sql.expression import false
from sqlalchemy.sql.functions import mode
from helpers import convert_to_dict
from database import SessionLocal
import models
from services import storage

db = SessionLocal()


def add_new_product(shop_id):
    shop = db.query(models.Shop).filter(models.Shop.id == shop_id).first()

    p1 = models.Product()
    p1.name = input('Unesite ime product-a: ')
    p1.typee = input('Unesite tip product-a: ')
    p1.price = float(input('Unesite cenu product-a: '))
    quantity = float(input('Unesite quantity product-a: '))
    p1.shop_id = shop_id
    if p1.typee in ('medicine', 'parking ticket'):
        p1.serial_number = input('Unesite serial number product-a: ')
    if shop.typee == "pharmacy" and p1.typee == "medicine":
        db.add(p1)
        db.commit()
        db.refresh(p1)
        db.close()
        print('Uspesno ste dodali medicine product')
    elif shop.typee != "pharmacy" and p1.typee == "medicine":
        print('Doslo je do greske pri upisivanju u bazi')
    elif shop.typee == "corner shop" and p1.typee == "cigarettes":
        db.add(p1)
        db.commit()
        db.refresh(p1)
        db.close()
    elif shop.typee != "corner shop" and p1.typee == "cigarettes":
        print('Doslo je do greske pri upisivanju u bazi')
    else:
        db.add(p1)
        db.commit()
        db.refresh(p1)
        db.close()
    add_new_storage(p1.id)


def get_all_products():
    products = db.query(models.Product).all()
    if not products:
        return False
    return products


def get_product_by_id(id):
    products = db.query(models.Product).filter(models.Product.id == id).first()
    if not products:
        return False
    return products


def update_product(id, newProduct):
    products = db.query(models.Product).filter(models.Product.id == id)

    if not products.first():
        return False

    products.update(convert_to_dict(newProduct), synchronize_session=False)
    db.commit()
    return True


def delete_product(id):
    product = db.query(models.Product).filter(models.Product.id == id)

    if not product.first():
        return False

    product.delete()
    db.commit()
    return True


# CRUD FOR STORAGE

def get_quantity_by_product_id(id):
    products = db.query(models.Storage).filter(
        models.Storage.id == products.id).first()
    if not products:
        return False
    return products


def update_quantity(id, newStorage):
    products = db.query(models.Storage).filter(models.Storage.id == id)

    if not products.first():
        return False

    products.update(convert_to_dict(newStorage), synchronize_session=False)
    db.commit()
    return True
