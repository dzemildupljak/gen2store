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

    if product.typee in ('medicine','parking ticket'):
        product.serial_number = input('unesi serijski broj:')

    if shop.typee == 'pharmacy' and product.typee == 'medicine':
        db.add(product)
        db.commit()
        db.close() 
        return 'done!'
    elif shop.typee != 'pharmacy' and product.typee == 'medicine':
        print('mistake')
    elif shop.typee == 'corner shop' and product.typee == 'cigarettes':
        db.add(product)
        db.commit()
        db.close() 
        return 'done!'
    else:
        print('mistake')


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
    products = db.query(models.Product).filter(models.Product.id == id )

    if not products.first():
        return False

    products.update(convert_to_dict(newProduct), synchronize_session=False)
    db.commit()
    return True

# kada hocu da potvrdim ono sto sam radila
# git commit -m "poruka za onon sto sam radila"


# kada zavrsim i sigrna sam da je to ok
# git push origin ab/crud_product
