from sqlalchemy import String, Column, DateTime, Integer, Float
from app.database import Base


class User(Base):
    __tablename__ = "users"
    profile_id = Column(
        String,
        primary_key=True,
        unique=True,
        nullable=False,
        index=True,
    )
    name = Column(String, index=True)
    email = Column(String, index=True)


class Awards(Base):
    __tablename__ = "Awards"
    profile_id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        index=True,
    )
    program = Column(String, index=True)
    name = Column(String, index=True)
    rent_arrears_plan_form_date = Column(DateTime, index=True)
    total_client_arrears_90_plus_days_old = Column(Float, index=True)
    arrears_plan = Column(String, index=True)
    erap_application_submitted = Column(String, index=True)
    erap_application_date = Column(DateTime, index=True)
    erap_confirmation = Column(String, index=True)
    erap_application_status = Column(String, index=True)
    erap_status_date = Column(DateTime, index=True)
    erap_payment_received = Column(String, index=True)
    erap_amount_received = Column(Integer, index=True)
    erap_denied = Column(String, index=True)
    osd_application_submitted = Column(String, index=True)
    osd_application_date = Column(DateTime, index=True)
    osd_confirmation = Column(String, index=True)
    osd_application_status = Column(String, index=True)
    osd_status_date = Column(DateTime, index=True)
    osd_payment_received = Column(String, index=True)
    osd_payment_amount = Column(Integer, index=True)
    homebase_linkages = Column(String, index=True)
    homebase_provider = Column(String, index=True)
    is_client_receiving_ssi = Column(String, index=True)
    ssi_rep_payee = Column(String, index=True)
    case_manger_conference = Column(String, index=True)
    date_of_case_manger_Conf = Column(DateTime, index=True)
    rep_payee = Column(String, index=True)
    voluntary_up_rep_payee = Column(String, index=True)
    type_of_entitlement_issue = Column(String, index=True)
    outcome_of_cmc = Column(String, index=True)
    pm_case_conference = Column(String, index=True)
    pm_case_conference_date = Column(DateTime, index=True)
    pl_cc_outcome = Column(String, index=True)
    ecc = Column(String, index=True)
    ecc_date = Column(DateTime, index=True)
    ecc_outcome = Column(String, index=True)
    housing_court_action = Column(String, index=True)
    date_of_referral_to_housing_counsel = Column(String, index=True)
    date_letter_595_discharge = Column(DateTime, index=True)
    notice_595_housing_action = Column(String, index=True)
    start_date_of_payment_plan = Column(DateTime, index=True)
    repayment_plan_amount = Column(String, index=True)
    rent_arrears_plan_note = Column(String, index=True)
