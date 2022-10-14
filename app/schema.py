from pydantic import BaseModel, constr, EmailStr
from typing import Optional


class OrmMode(BaseModel):
    class Config:
        orm_mode = True


class SchemaOnePoint(OrmMode):
    profile_id: int
    property: str
    resh_id: str
    lease_id: str
    bldg_unit: str
    name: str
    phone_number: str
    email: str
    status: str
    move_in_out: str
    code_description: str
    total_prepaid: str
    total_delinquent: str
    d: str
    o: str
    net_balance: str
    current: str
    days_30: str
    days_60: str
    days_90_plus: str
    prorate_credit: str
    deposits_held: str
    outstanding_deposit: str
    late: str
    nsf: str
    delinquency_comment: str
    comment_date: str
    leasing_agent: str


class SchemaAwards(OrmMode):
    profile_id: int
    program: str
    name: str
    rent_arrears_plan_form_date: Optional[str]
    total_client_arrears_90_plus_days_old: Optional[str]
    arrears_plan: Optional[str]
    erap_app_submitted: Optional[str]
    erap_app_date: Optional[str]
    erap_confirmation_number: Optional[str]
    erap_app_status: Optional[str]
    erap_status_date: Optional[str]
    erap_payment_received: Optional[str]
    erap_amount_received: Optional[str]
    erap_denied: Optional[str]
    osd_app_submitted: Optional[str]
    osd_app_date: Optional[str]
    osd_confirmation_number: Optional[str]
    osd_app_status: Optional[str]
    osd_status_date: Optional[str]
    osd_payment_received: Optional[str]
    osd_payment_amount: Optional[str]
    homebase_linkages: Optional[str]
    homebase_provider: Optional[str]
    ssi: Optional[str]
    ssi_rep_payee: Optional[str]
    case_manager_conference: Optional[str]
    cmc_date: Optional[str]
    rep_payee: Optional[str]
    voluntary_up_rep_payee: Optional[str]
    type_of_entitlement_issue: Optional[str]
    cmc_outcome: Optional[str]
    pm_case_conference: Optional[str]
    pm_cc_date: Optional[str]
    pl_cc_outcome: Optional[str]
    ecc: Optional[str]
    ecc_date: Optional[str]
    ecc_outcome: Optional[str]
    housing_court_action: Optional[str]
    housing_counsel_referral_date: Optional[str]
    date_letter_595_discharge: Optional[str]
    notice_595_housing_action: Optional[str]
    payment_plan_start_date: Optional[str]
    repayment_plan_amount: Optional[str]
    rent_arrears_plan_note: Optional[str]

