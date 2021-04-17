import datetime
import uuid
from sqlalchemy.sql.expression import false
from helpers import convert_to_dict
from database import SessionLocal
import models

db = SessionLocal()


def add_new_bill(c_id):
    customer = db.query(models.Customer).filter(models.Customer.id == c_id)
    if customer.first():
        return false
    b1 = models.Bill()
    b1.bill_number = uuid.uuid1()
    b1.customer_id = c_id
    b1.bill_date = datetime.datetime.now()

    try:
        db.add(b1)
        db.commit()
        db.close()
    except:
        print('Doslo je do greske pri upisivanju u bazi')


def get_all_bills():
    bills = db.query(models.Bill).all()
    if not bills:
        return False
    return bills


def get_bill_by_id(id):
    bills = db.query(models.Bill).filter(models.Bill.id == id).first()
    if not bills:
        return False
    return bills


def get_bill_by_uuid(uuid):
    bills = db.query(models.Bill).filter(
        models.Bill.bill_number == uuid).first()
    if not bills:
        return False
    return bills


def update_Bill(id, newBill):
    bills = db.query(models.Bill).filter(models.Bill.id == id)

    if not bills.first():
        return False

    bills.update(convert_to_dict(newBill), synchronize_session=False)
    db.commit()
    return True


def delete_bill(id):
    bill = db.query(models.Bill).filter(models.Bill.id == id)

    if not bill.first:
        return False

    bill.delete()
    db.commit()
    return True
