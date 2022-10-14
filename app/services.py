from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.table_models import OnepointUser, AwardsUser
from app.schema import SchemaOnePoint, SchemaAwards
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
    return db.query(OnepointUser).filter(OnepointUser.profile_id == profile_id).first()


def read_onepoint_users(db: Session):
    return db.query(OnepointUser).all()


def read_awards_users(db: Session):
    return db.query(AwardsUser).all()


def create_user(db: Session, user: SchemaOnePoint):
    db_user = OnepointUser(
        profile_id=user.profile_id,
        name=user.name,
        email=user.email,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, profile_id: str, update_data: Dict) -> str:
    db.query(OnepointUser).filter(
        OnepointUser.profile_id == profile_id
    ).update(update_data)
    db.commit()
    return f"User {profile_id} has been updated with {update_data}"


def delete_user(db: Session, profile_id: str):
    db.query(OnepointUser).filter(
        OnepointUser.profile_id == profile_id
    ).delete()
    db.commit()
    return f"User {profile_id} has been deleted"


def nuclear_launch_detected(db: Session):
    db.query(OnepointUser).delete()
    db.query(AwardsUser).delete()
    db.commit()
