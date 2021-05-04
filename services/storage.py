from models import Storage
from helpers import convert_to_dict
from database import SessionLocal, db


def get_product_quantity_from_storage(prod_id):
    try:
        product = db.query(Storage).filter(
            Storage.product_id == prod_id).first()
        return product.quantity
    except:
        print("Error!")
        return False


def update_storage(prod_id, newProduct):
    try:
        product = db.query(Storage).filter(Storage.prod_id == prod_id)
        product.update(convert_to_dict(newProduct), synchronize_session=False)
        db.commit()
        return True
    except:
        print("Error!")
        return False


def add_new_storage(prod_id, qn):
    try:
        s1 = Storage()
        s1.product_id = prod_id
        s1.quantity = qn
        db.add(s1)
        db.commit()
        db.close()
        print('Uspesno ste dodali product')
    except:
        print("Error")
