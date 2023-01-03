from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.table_models import User
from app.schema import SchemaUser
from typing import Dict


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)


def read_first(db: Session, profile_id: str):
    return db.query(User).filter(User.profile_id == profile_id).first()


def read_users(db: Session):
    return db.query(User).all()
