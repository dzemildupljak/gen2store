from database import engine, SessionLocal
import models
from services import shop, product, bill, customer, storage
db = SessionLocal()
models.Base.metadata.create_all(engine)
# TODO bill number da se sredi sa uuid,DA SE DODA LISTA PRODUCATA U BILL
# da se macinje space na broj telefona customera
# db.query(models.Product).filter(models.Product.id == 5).delete()
# db.commit()
# shop.add_new_shop()
# product.add_new_product(1)
# product.add_new_product(1)
# product.add_new_product(2)
# product.add_new_product(2)
# product.add_new_product(3)
# product.add_new_product(3)
# customer.add_new_customer()

# a = bill.add_new_bill(1)
# print(a)
