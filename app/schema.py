from datetime import datetime

from pydantic import BaseModel, constr, EmailStr
from typing import Optional
from datetime import datetime

from sqlalchemy import DateTime


class OrmMode(BaseModel):
    class Config:
        orm_mode = True


class SchemaUser(OrmMode):
    profile_id: str
    name: constr(max_length=255)
    email: EmailStr


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


class SchemaOnesite(OrmMode):
    profile_id: int
    property: Optional[str]
    resh_id: Optional[str]
    lease_id: Optional[str]
    building: Optional[str]
    name: Optional[str]
    phone_num: Optional[str]
    email: Optional[str]
    status: Optional[str]
    move_in: Optional[str]
    code: Optional[str]
    tot_prepay: Optional[float]
    tot_delq : Optional[float]
    D : Optional[str]
    O : Optional[str]
    net_bal : Optional[float]
    current : Optional[float]
    thirty_day : Optional[float]
    sixty_day : Optional[float]
    ninety_plus : Optional[float]
    prorate : Optional[float]
    deposits : Optional[float]
    outstanding : Optional[float]
    num_late : Optional[int]
    num_nsf : Optional[int] 
    delq_comment : Optional[str]
    comment_date : Optional[str]
    leasing_agent : Optional[str]
