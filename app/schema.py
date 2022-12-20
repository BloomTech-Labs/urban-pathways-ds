from pydantic import BaseModel, constr, EmailStr
from typing import Optional
from datetime import datetime


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


class SchemaCreateOnesiteDB(OrmMode): 
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
