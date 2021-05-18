from database import SessionLocal
from models import Storage
from helpers import convert_to_dict


db = SessionLocal()


def get_product_quantity_from_storage_by_id(prod_id):
    product = db.query(Storage).filter(Storage.product_id == prod_id).first()
    return product.quantity


def update_storage(prod_id, newStorage):
    product = db.query(Storage).filter(Storage.prod_id == prod_id)
    product.update(convert_to_dict(newStorage), synchronize_session=False)
    db.commit()


def add_new_storage(product_id):
    s1 = Storage()
    s1.quantity = input('Unesite quantity: ')
    s1.product_id = product_id
    db.add(s1)
    db.commit()
    db.close()
