from database import engine
import models
from services import shop

models.Base.metadata.create_all(engine)

shop.add_new_shop()
