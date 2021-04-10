from database import SessionLocal
from models import Shop


db = SessionLocal()


def add_new_shop():
    s1 = Shop()
    s1.name = input('Unesite ime shop-a: ')
    while s1.type not in ('supermarket', 'cornershop', 'pharmacy'):
        s1.type = input('Unesite tip shop-a: ')
    try:
        db.add(s1)
        db.commit()
        db.close()
    except:
        print('Doslo je do greske pri upisivanju u bazi')


def get_all_shops():
    shops = db.query(Shop).all()
    if not shops:
        return False
    return shops

