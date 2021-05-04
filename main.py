from database import engine, SessionLocal
import models
from services import shop, product, bill
db = SessionLocal()
models.Base.metadata.create_all(engine)

# db.query(models.Product).filter(models.Product.id == 5).delete()
# db.commit()
# shop.add_new_shop()
product.add_new_product(1)
# product.add_new_product(1)
# product.add_new_product(2)
# product.add_new_product(2)
# product.add_new_product(3)
# product.add_new_product(3)


# bill.add_new_bill((c_id))
