from helpers import convert_to_dict
from database import SessionLocal
import models

db = SessionLocal()


def add_new_customer():
    
    c1 = models.Customer()
    c1.firstname = input('Unesite ime customera: ')
    c1.lastname = input('Unesite prezime customera: ')
    c1.telephone_number = input('Unesite broj telefona:')
    c1.points = int(input('Unesite poene: '))

    db.add(c1)
    db.commit()
    db.close()


def get_all_customers():
    customers = db.query(models.Customer).all()
    if not customers:
        return False
    return customers


def get_customer_by_id(id):
    customers = db.query(models.Customer).filter(models.Customer.id == id).first()
    if not customers:
        return False
    return customers


def update_customer(id, newCustomer):
    customers = db.query(models.Customer).filter(models.Customer.id == id)

    if not customers.first():
        return False

    customers.update(convert_to_dict(newCustomer), synchronize_session=False)
    db.commit()
    return True


def delete_customer(id):
    customer = db.query(models.Customer).filter(models.Customer.id == id)

    if not customer.first:
        return False

    customer.delete()
    db.commit()
    return True
