from services.product import get_product_by_id, update_product


def sell_product(prod_id, qty):
    product = get_product_by_id(prod_id)
    if product.quantity < qty:
        return False
    product.quantity -= qty
    return update_product(prod_id, product)


def POS():
    print(get_all_shop())
    shop = get_by_id_shop(int(input("Unesite id shop-a !")))
    products = get_product_by_shop_id(shop.id)
    odabir = input("1.ADD TO CART\n2.EXIT").upper()
    if odabir in ("1", "ADD TO CART"):
        print(products)
        # unos id producta i dodavnje u korpu
        while True:
            odabir = input("1.CONTINUE SHOPPING\n2.PAY\n3.EXIT").upper()
            if odabir in ("1", "CONTINUE SHOPPING"):
                print(products)
                # unos id producta i dodavnje u korpu
            elif odabir in ("2", "PAY"):
                cust_id = add_new_customer()
                add_new_bill(cust_id)
                print("Hvala na poseti!")
                break
            elif odabir in ("3", "EXIT"):
                break

    elif odabir in ("2", "EXIT"):
        print("Hvala na poseti")
