from sqlalchemy import String, Column, Date, Float, Integer, DateTime
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


class OneSiteData(Base):
    __tablename__ = "OneSiteData"
    profile_id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        index=True,
    )
    property = Column(String, index = True)
    resh_id = Column(String, index = True)
    lease_id = Column(String, index = True)
    building = Column(String, index = True)
    name = Column(String, index = True)
    phone_num = Column(String, index = True)
    email = Column(String, index = True)
    status = Column(String, index = True)
    move_in = Column(String, index = True)
    code = Column(String, index = True)
    tot_prepay = Column(Float, index = True)
    tot_delq = Column(Float, index = True)
    D = Column(String, index = True)
    O = Column(String, index = True)
    net_bal = Column(Float, index = True)
    current = Column(Float, index = True)
    thirty_day = Column(Float, index = True)
    sixty_day = Column(Float, index = True)
    ninety_plus = Column(Float, index = True)
    prorate = Column(Float, index = True)
    deposits = Column(Float, index = True)
    outstanding = Column(Float, index = True)
    num_late = Column(Integer, index = True)
    num_nsf = Column(Integer, index = True)
    delq_comment = Column(String, index = True)
    comment_date = Column(String, index = True)
    leasing_agent = Column(String, index = True)
