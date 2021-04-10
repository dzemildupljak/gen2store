from database import engine
import models
from services import add_new_shop, get_all_shops

models.Base.metadata.create_all(engine)
