
def sell_product(id, sq):
    p1 = get_product_by_id(id)
    if product.quantity < sq:
        return False
    p1.quantity -= sq
    return update_product(id, p1)