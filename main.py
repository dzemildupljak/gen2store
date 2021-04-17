from database import engine
import models
from services import shop, product, bill

models.Base.metadata.create_all(engine)
