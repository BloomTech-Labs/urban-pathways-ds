from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.table_models import User, OneSiteData
from app.schema import SchemaUser
from typing import Dict
from fastapi import File, UploadFile
import xlrd as xlrd
import os
from io import BytesIO
import mmap


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)


def read_first(db: Session, profile_id: str):
    return db.query(User).filter(User.profile_id == profile_id).first()


def read_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: SchemaUser):
    db_user = User(
        profile_id=user.profile_id,
        name=user.name,
        email=user.email,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, profile_id: str, update_data: Dict) -> str:
    db.query(User).filter(
        User.profile_id == profile_id
    ).update(update_data)
    db.commit()
    return f"User {profile_id} has been updated with {update_data}"


def delete_user(db: Session, profile_id: str):
    db.query(User).filter(
        User.profile_id == profile_id
    ).delete()
    db.commit()
    return f"User {profile_id} has been deleted"


def save_onesite_data(db: Session, file: UploadFile = File(...)):
    filepath = os.path.realpath(os.path.join("fixtures", file.filename))
    excel_workbook = xlrd.open_workbook(filepath)
    all_worksheet = excel_workbook.sheet_by_name("All")
    curr_worksheet = excel_workbook.sheet_by_name("Curr")
    curr_row = 3

    while curr_row < curr_worksheet.nrows-1:
        curr_row += 1 
        row = curr_worksheet.row_values(curr_row)
        db_OneSite = OneSiteData(
            property=row[0],
            resh_id=row[1],
            lease_id=row[2],
            building=row[3],
            name=row[4],
            phone_num=row[5],
            email=row[6],
            status=row[7],
            move_in=row[8],
            code=row[9],
            tot_prepay=row[10],
            tot_delq=row[11],
            D =row[12],
            O =row[13],
            net_bal=row[14],
            current=row[15],
            thirty_day=row[16],
            sixty_day=row[17],
            ninety_plus=row[18],
            prorate=row[19],
            deposits=row[20],
            outstanding=row[21],
            num_late=row[22],
            num_nsf=row[23],
            delq_comment=row[24],
            comment_date=row[25],
            leasing_agent=row[26]
        )
        db.add(db_OneSite)
        db.commit()

    return {"You've successfully loaded":file.filename}
