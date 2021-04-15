from database import engine
import models
from services import shop, product,

models.Base.metadata.create_all(engine)

shop.add_new_shop()
product.add_new_product