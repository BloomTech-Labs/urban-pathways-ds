from sqlalchemy import String, Column, Integer
from app.database import Base


class OnepointUser(Base):
    __tablename__ = "one_point_users"
    profile_id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        index=True,

    )
    property = Column(String, index=True)
    resh_id = Column(String, index=True)
    lease_id = Column(String, index=True)
    bldg_unit = Column(String, index=True)
    name = Column(String, index=True)
    phone_number = Column(String, index=True, nullable=True)
    email = Column(String, index=True, nullable=True)
    status = Column(String, index=True, nullable=True)
    move_in_out = Column(String, index=True, nullable=True)
    code_description = Column(String, index=True, nullable=True)
    total_prepaid = Column(String, index=True, nullable=True)
    total_delinquent = Column(String, index=True, nullable=True)
    d = Column(String, index=True, nullable=True)
    o = Column(String, index=True, nullable=True)
    net_balance = Column(String, index=True, nullable=True)
    current = Column(String, index=True, nullable=True)
    days_30 = Column(String, index=True, nullable=True)
    days_60 = Column(String, index=True, nullable=True)
    days_90_plus = Column(String, index=True, nullable=True)
    prorate_credit = Column(String, index=True, nullable=True)
    deposits_held = Column(String, index=True, nullable=True)
    outstanding_deposit = Column(String, index=True, nullable=True)
    late = Column(String, index=True, nullable=True)
    nsf = Column(String, index=True, nullable=True)
    delinquency_comment = Column(String, index=True, nullable=True)
    comment_date = Column(String, index=True, nullable=True)
    leasing_agent = Column(String, index=True, nullable=True)


class AwardsUser(Base):
    __tablename__ = "awards_users"
    profile_id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        index=True,
    )
    program = Column(String, index=True)
    name = Column(String, index=True)
    rent_arrears_plan_form_date = Column(String, index=True, nullable=True)
    total_client_arrears_90_plus_days_old = Column(String, index=True, nullable=True)
    arrears_plan = Column(String, index=True, nullable=True)
    erap_app_submitted = Column(String, index=True, nullable=True)
    erap_app_date = Column(String, index=True, nullable=True)
    erap_confirmation_number = Column(String, index=True, nullable=True)
    erap_app_status = Column(String, index=True, nullable=True)
    erap_status_date = Column(String, index=True, nullable=True)
    erap_payment_received = Column(String, index=True, nullable=True)
    erap_amount_received = Column(String, index=True, nullable=True)
    erap_denied = Column(String, index=True, nullable=True)
    osd_app_submitted = Column(String, index=True, nullable=True)
    osd_app_date = Column(String, index=True, nullable=True)
    osd_confirmation_number = Column(String, index=True, nullable=True)
    osd_app_status = Column(String, index=True, nullable=True)
    osd_status_date = Column(String, index=True, nullable=True)
    osd_payment_received = Column(String, index=True, nullable=True)
    osd_payment_amount = Column(String, index=True, nullable=True)
    homebase_linkages = Column(String, index=True, nullable=True)
    homebase_provider = Column(String, index=True, nullable=True)
    ssi = Column(String, index=True, nullable=True)
    ssi_rep_payee = Column(String, index=True, nullable=True)
    case_manager_conference = Column(String, index=True, nullable=True)
    cmc_date = Column(String, index=True, nullable=True)
    rep_payee = Column(String, index=True, nullable=True)
    voluntary_up_rep_payee = Column(String, index=True, nullable=True)
    type_of_entitlement_issue = Column(String, index=True, nullable=True)
    cmc_outcome = Column(String, index=True, nullable=True)
    pm_case_conference = Column(String, index=True, nullable=True)
    pm_cc_date = Column(String, index=True, nullable=True)
    pl_cc_outcome = Column(String, index=True, nullable=True)
    ecc = Column(String, index=True, nullable=True)
    ecc_date = Column(String, index=True, nullable=True)
    ecc_outcome = Column(String, index=True, nullable=True)
    housing_court_action = Column(String, index=True, nullable=True)
    housing_counsel_referral_date = Column(String, index=True, nullable=True)
    date_letter_595_discharge = Column(String, index=True, nullable=True)
    notice_595_housing_action = Column(String, index=True, nullable=True)
    payment_plan_start_date = Column(String, index=True, nullable=True)
    repayment_plan_amount = Column(String, index=True, nullable=True)
    rent_arrears_plan_note = Column(String, index=True, nullable=True)
