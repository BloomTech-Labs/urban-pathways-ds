import openpyxl as openpyxl
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.table_models import User, Awards
from app.schema import SchemaUser
from typing import Dict
from fastapi import File, UploadFile
import os


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


def read_awards(db: Session):
    return db.query(Awards).all()


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


def save_awards_data(db: Session, f: UploadFile = File(...)):
    f = os.path.realpath(os.path.join("fixtures", f.filename))
    awards_file = openpyxl.load_workbook(f)
    awards_sheet = awards_file.active
    rows = awards_sheet.iter_rows(13, 3000, 0, 43, values_only=True)
    values = [row for row in rows]
    for row in values:
        if row[0] is None:
            break
        else:
            a_users = Awards(
                program=row[0],
                name=row[1],
                rent_arrears_plan_form_date=row[2],
                total_client_arrears_90_plus_days_old = remove_multiple_periods(row[3]),
                arrears_plan=row[4],
                erap_application_submitted=row[5],
                erap_application_date=row[6],
                erap_confirmation=row[7],
                erap_application_status=row[8],
                erap_status_date=row[9],
                erap_payment_received=row[10],
                erap_amount_received=row[11],
                erap_denied=row[12],
                osd_application_submitted=row[13],
                osd_application_date=row[14],
                osd_confirmation=row[15],
                osd_application_status=row[16],
                osd_status_date=row[17],
                osd_payment_received=row[18],
                osd_payment_amount=row[19],
                homebase_linkages=row[20],
                homebase_provider=row[21],
                is_client_receiving_ssi=row[22],
                ssi_rep_payee=row[23],
                case_manger_conference=row[24],
                date_of_case_manger_Conf=row[25],
                rep_payee=row[26],
                voluntary_up_rep_payee=row[27],
                type_of_entitlement_issue=row[28],
                outcome_of_cmc=row[29],
                pm_case_conference=row[30],
                pm_case_conference_date=row[31],
                pl_cc_outcome=row[32],
                ecc=row[33],
                ecc_date=row[34],
                ecc_outcome=row[35],
                housing_court_action=row[36],
                date_of_referral_to_housing_counsel=row[37],
                date_letter_595_discharge=row[38],
                notice_595_housing_action=row[39],
                start_date_of_payment_plan=row[40],
                repayment_plan_amount=row[41],
                rent_arrears_plan_note=row[42]

            )
            db.add(a_users)
        db.commit()


def remove_multiple_periods(text):
    if isinstance(text, int):
        return float(text)
    if isinstance(text, float):
        return text
    while ".." in text:
        text = text.replace("..", ".")
    text = text.replace("$", "")
    return float(text)



if __name__ == '__main__':
    import requests

    q = requests.get("http://127.0.0.1:8000/")
    op_users = requests.get("http://127.0.0.1:8000/read-awards/")
    print(op_users.json())