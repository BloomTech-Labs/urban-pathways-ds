from sqlalchemy import String, Column
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