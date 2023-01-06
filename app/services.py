from io import BytesIO
import openpyxl
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.table_models import User, OneSiteData, Awards
from app.schema import SchemaUser
from typing import Dict
from fastapi import File, UploadFile
import xlrd as xlrd
import os
from io import BytesIO


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


def read_onesite(db: Session):
    return db.query(OneSiteData).all()


def save_onesite_data(db: Session, file: UploadFile = File(...)):
    filepath = os.path.realpath(os.path.join("fixtures", file.filename))
    excel_workbook = xlrd.open_workbook(filepath)
    all_worksheet = excel_workbook.sheet_by_name("All")
    curr_worksheet = excel_workbook.sheet_by_name("Curr")
    curr_row = 3

    while curr_row < curr_worksheet.nrows - 1:
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
            D=row[12],
            O=row[13],
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

    return {"You've successfully loaded": file.filename}


def save_awards_data(db: Session, file: UploadFile = File(...)):
    awards_file = openpyxl.load_workbook(BytesIO(file.file.read()))
    awards_sheet = awards_file.active
    max_rows = awards_sheet.max_row
    rows = awards_sheet.iter_rows(13, max_rows, 0, 43, values_only=True)
    values = [row for row in rows]
    for row in values:
        if row[0] is None:
            break
        else:
            a_users = Awards(
                program=row[0],
                name=row[1],
                rent_arrears_plan_form_date=row[2],
                total_client_arrears_90_plus_days_old=remove_multiple_periods(row[3]),
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
    return {"You've successfully loaded": file.filename}


def remove_multiple_periods(text):
    if isinstance(text, int):
        return float(text)
    if isinstance(text, float):
        return text
    while ".." in text:
        text = text.replace("..", ".")
    text = text.replace("$", "")
    return float(text)
