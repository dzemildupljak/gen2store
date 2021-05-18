from database import engine
import models
from services import shop, product, bill
models.Base.metadata.create_all(engine)


# shop1 = shop.add_new_shop()
# if shop1:
#     product.add_new_product(shop1.id)

# product.add_new_product()

# product.delete_product(1)
