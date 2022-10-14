import sys

import openpyxl
import pandas as pd
import xlrd
import sys
from sqlalchemy.orm import Session
from app.table_models import OnepointUser, AwardsUser


# awards_fp = "fixtures/AWARDS Rent Arrears Plan Summary - 7.1.22_8.31.22.xlsx"
# onesite_fp = "fixtures/Urban_Pathways-Aug_2022_All_Delq-PP.xls"


def read_xls(filepath: str, db: Session):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name("All")
    num_rows = worksheet.nrows - 1
    curr_row = 3
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        values = [item.value for item in row]
        op_user = OnepointUser(
            property=values[0],
            resh_id=values[1],
            lease_id=values[2],
            bldg_unit=values[3],
            name=values[4],
            phone_number=values[5],
            email=values[6],
            status=values[7],
            move_in_out=values[8],
            code_description=values[9],
            total_prepaid=values[10],
            total_delinquent=values[11],
            d=values[12],
            o=values[13],
            net_balance=values[14],
            current=values[15],
            days_30=values[16],
            days_60=values[17],
            days_90_plus=values[18],
            prorate_credit=values[19],
            deposits_held=values[20],
            outstanding_deposit=values[21],
            late=values[22],
            nsf=values[23],
            delinquency_comment=values[24],
            comment_date=values[25],
            leasing_agent=values[26],
        )
        db.add(op_user)
    db.commit()

#
# def read_xlsx(filepath: str):
#     workbook = openpyxl.load_workbook(filepath)
#     ws = workbook.active
#     num_rows = ws.
#     values = [value for row in ws.values for value in row]
#     print(values[0:2000])


def read_xlsx(filepath: str, db: Session):
    workbook = openpyxl.load_workbook(filepath)
    worksheet = workbook.active
    rows = worksheet.iter_rows(13, 300, 0, 43, values_only=True)
    values = [row for row in rows]
    for row in values:
        if row[0] is None:
            break
        else:
            a_user = AwardsUser(
                program=row[0],
                name=row[1],
                rent_arrears_plan_form_date=row[2],
                total_client_arrears_90_plus_days_old=row[3],
                arrears_plan=row[4],
                erap_app_submitted=row[5],
                erap_app_date=row[6],
                erap_confirmation_number=row[7],
                erap_app_status=row[8],
                erap_status_date=row[9],
                erap_payment_received=row[10],
                erap_amount_received=row[11],
                erap_denied=row[12],
                osd_app_submitted=row[13],
                osd_app_date=row[14],
                osd_confirmation_number=row[15],
                osd_app_status=row[16],
                osd_status_date=row[17],
                osd_payment_received=row[18],
                osd_payment_amount=row[19],
                homebase_linkages=row[20],
                homebase_provider=row[21],
                ssi=row[22],
                ssi_rep_payee=row[23],
                case_manager_conference=row[24],
                cmc_date=row[25],
                rep_payee=row[26],
                voluntary_up_rep_payee=row[27],
                type_of_entitlement_issue=row[28],
                cmc_outcome=row[29],
                pm_case_conference=row[30],
                pm_cc_date=row[31],
                pl_cc_outcome=row[32],
                ecc=row[33],
                ecc_date=row[34],
                ecc_outcome=row[35],
                housing_court_action=row[36],
                housing_counsel_referral_date=row[37],
                date_letter_595_discharge=row[38],
                notice_595_housing_action=row[39],
                payment_plan_start_date=row[40],
                repayment_plan_amount=row[41],
                rent_arrears_plan_note=row[42],
            )
            db.add(a_user)
        db.commit()


if __name__ == '__main__':
    # pandas_read_xls("fixtures/Urban_Pathways-Aug_2022_All_Delq-PP.xls")
    # read_xlsx("fixtures/AWARDS Rent Arrears Plan Summary - 7.1.22_8.31.22.xlsx")

    import requests
    q = requests.get("http://127.0.0.1:8000/")
    op_users = requests.get("http://127.0.0.1:8000/read-onepoint-users/")
    a_users = requests.get("http://127.0.0.1:8000/read-awards-users/")
    print(op_users.json())
    print(a_users.json())
