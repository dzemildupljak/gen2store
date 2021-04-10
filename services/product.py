import models
from database import SessionLocal
 db
#C
def add_new_product(shop_id,name,typ,price):

    shop = db.query(models.Shop).filter(models.Shop.id == id)
    product = models.Product()
    product.name = name
    product.typee = typ
    product.price = price

    if shop.typee == 'pharmacy' and product.typee == 'medicine':
        db.add(product)
        db.commit()
        db.close() 
        return 'done!'

def get_all():
    products = db.query(models.Product).all()
    if not products:
        return False
    return products


def get_by_id(id):
    product = db.query(models.Product).filter(models.Product.id == id ).first()
    if not product :
        return False
    return product


def delete_product(id):
    products = db.query(models.Product).filter(models.Product.id == id )

    if not products.first:
        return False

    products.delete()
    db.commit()
    return True

def update_product():


