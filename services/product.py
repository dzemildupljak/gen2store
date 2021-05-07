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
    p1.price = float(input('Unesite cenu product-a: '))
    p1.shop_id = shop_id
    if shop.typee == "Pharmacy":
        while p1.typee not in ("Food", "Drink", "Medicine",  "Parking ticket", "Toys"):
            print(
                "Available types: FOOD ; DRINK ; MEDICINE ; PARKING TICKETS ; TOYS")
            p1.typee = input('Unesite tip product-a: ').capitalize()
    elif shop.typee == "Corner shop":
        while p1.typee not in ("Food", "Drink", "Cigarettes",  "Parking ticket", "Toys"):
            print(
                "Available types: FOOD ; DRINK ; CIGARETTES ; PARKING TICKETS ; TOYS")
            p1.typee = input('Unesite tip product-a: ').capitalize()
    elif shop.typee == "supermarket":
        while p1.typee not in ("Food", "Drink", "Parking ticket", "Toys"):
            print(
                "Available types: FOOD ; DRINK ; PARKING TICKETS ; TOYS")
            p1.typee = input('Unesite tip product-a: ').capitalize()
    else:
        print("Error")
    if p1.typee in ('medicine', 'parking ticket'):
        p1.serial_number = input('Unesite serial number product-a: ')
    if shop.typee == "pharmacy" and p1.typee == "medicine":
        db.add(p1)
        db.commit()
        db.refresh(p1)
        odabir = input("Unos quantity\n1.DA 2.NE").capitalize()
        if odabir in ("Ne", "2"):
            try:
                storage.add_new_storage(p1.id)
            except:
                print("Error!")
        elif odabir in ("Da", "1"):
            try:
                storage.add_new_storage(
                    p1.id, qn=int(input("Unesite quantity: ")))
            except:
                print("Error!")

    elif shop.typee != "pharmacy" and p1.typee == "medicine":
        print('Medicine mozete dodati samo u shop sa tipom Pharmacy!')

    elif shop.typee == "cornershop" and p1.typee == "cigarettes":
        db.add(p1)
        db.commit()
        db.refresh(p1)
        odabir = input("Unos quantity\n1.DA 2.NE").capitalize()
        if odabir in ("Ne", "2"):
            try:
                storage.add_new_storage(p1.id)
            except:
                print("Error!")
        if odabir in ("Da", "1"):
            try:
                storage.add_new_storage(
                    p1.id, qn=int(input("Unesite quantity: ")))
            except:
                print("Error!")
    elif shop.typee != "cornershop" and p1.typee == "cigarettes":
        print('Cigarettes mozete dodati samo u shop sa tipom Cornershop')
    else:
        odabir = input("Unos quantity\n1.DA 2.NE").capitalize()
        if odabir in ("Ne", "2"):
            try:
                storage.add_new_storage(p1.id, None)
            except:
                print("Error!")
        if odabir in ("Da", "1"):
            try:
                storage.add_new_storage(
                    p1.id, qn=int(input("Unesite quantity: ")))
            except:
                print("Error!")


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


def get_product_by_id(shop_id):
    products = db.query(models.Product).filter(
        models.Product.shop_id == shop_id).all()
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
    product = db.query(models.Shop).filter(models.Shop.id == id)

    if not product.first:
        return False

    product.delete()
    db.commit()
    return True
