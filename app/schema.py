from pydantic import BaseModel, constr, EmailStr
from typing import Optional


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




