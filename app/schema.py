from pydantic import BaseModel, constr, EmailStr
from typing import Optional


class OrmMode(BaseModel):
    class Config:
        orm_mode = True
