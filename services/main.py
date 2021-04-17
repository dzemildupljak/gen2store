from services.product import get_product_by_id, update_product


def sell_product(prod_id, qty):
    product = get_product_by_id(prod_id)
    if product.quantity < qty:
        return False
    product.quantity -= qty
    return update_product(prod_id, product)


def POS():
    pass
