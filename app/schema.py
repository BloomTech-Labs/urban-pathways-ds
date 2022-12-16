from datetime import datetime

from pydantic import BaseModel, constr, EmailStr
from typing import Optional

from sqlalchemy import DateTime


class OrmMode(BaseModel):
    class Config:
        orm_mode = True


class SchemaUser(OrmMode):
    profile_id: str
    name: constr(max_length=255)
    email: EmailStr


class SchemaUpdateUser(OrmMode):
    name: Optional[constr(max_length=255)]
    email: Optional[EmailStr]


class SchemaAwards(OrmMode):
    profile_id: int
    program: str
    name: str
    rent_arrears_plan_form_date: Optional[datetime]
    total_client_arrears_90_plus_days_old: Optional[float]
    arrears_plan: Optional[str]
    erap_app_submitted: Optional[str]
    erap_app_date: Optional[str]
    erap_confirmation_number: Optional[str]
    erap_app_status: Optional[str]
    erap_status_date: Optional[datetime]
    erap_payment_received: Optional[str]
    erap_amount_received: Optional[int]
    erap_denied: Optional[str]
    osd_app_submitted: Optional[str]
    osd_app_date: Optional[datetime]
    osd_confirmation_number: Optional[str]
    osd_app_status: Optional[str]
    osd_status_date: Optional[datetime]
    osd_payment_received: Optional[str]
    osd_payment_amount: Optional[int]
    homebase_linkages: Optional[str]
    homebase_provider: Optional[str]
    ssi: Optional[str]
    ssi_rep_payee: Optional[str]
    case_manager_conference: Optional[str]
    cmc_date: Optional[datetime]
    rep_payee: Optional[str]
    voluntary_up_rep_payee: Optional[str]
    type_of_entitlement_issue: Optional[str]
    cmc_outcome: Optional[str]
    pm_case_conference: Optional[str]
    pm_cc_date: Optional[datetime]
    pl_cc_outcome: Optional[str]
    ecc: Optional[str]
    ecc_date: Optional[datetime]
    ecc_outcome: Optional[str]
    housing_court_action: Optional[str]
    housing_counsel_referral_date: Optional[datetime]
    date_letter_595_discharge: Optional[str]
    notice_595_housing_action: Optional[str]
    payment_plan_start_date: Optional[datetime]
    repayment_plan_amount: Optional[str]
    rent_arrears_plan_note: Optional[str]

