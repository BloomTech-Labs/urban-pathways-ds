from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.table_models import OneSiteUser, AwardsUser
from typing import Dict


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    return Base.metadata.create_all(bind=engine)


def read_onesite_users(db: Session):
    return db.query(OneSiteUser).all()


def read_awards_users(db: Session):
    return db.query(AwardsUser).all()


def nuclear_launch_detected(db: Session):
    db.query(OneSiteUser).delete()
    db.query(AwardsUser).delete()
    db.commit()


