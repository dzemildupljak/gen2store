from helpers import convert_to_dict
from database import SessionLocal
import models

db = SessionLocal()


def add_new_bill(Bill_id,):
    bill = db.query(models.Bill).filer(models.Bill.id == Bill_id)

    b1 = models.bill()
    
    db.add(b1)
    db.commit()
    db.close()


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
