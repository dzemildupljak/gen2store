<<<<<<< HEAD

def sell_product(id, sq):
    p1 = get_product_by_id(id)
    if product.quantity < sq:
        return False
    p1.quantity -= sq
    return update_product(id, p1)
=======
from services.product import get_product_by_id, update_product


def sell_product(prod_id, qty):
    product = get_product_by_id(prod_id)
    if product.quantity < qty:
        return False
    product.quantity -= qty
    return update_product(prod_id, product)


def POS():
    pass
>>>>>>> 32a5043a423cc006b752c01bc7936b5f666ed4d1
