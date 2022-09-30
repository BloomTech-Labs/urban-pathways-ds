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


def create_user(db: Session, user: SchemaUser):
    db_user = User(
        profile_id=user.profile_id,
        name=user.name,
        email=user.email,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, profile_id: str, update_data: Dict) -> str:
    db.query(User).filter(
        User.profile_id == profile_id
    ).update(update_data)
    db.commit()
    return f"User {profile_id} has been updated with {update_data}"


def delete_user(db: Session, profile_id: str):
    db.query(User).filter(
        User.profile_id == profile_id
    ).delete()
    db.commit()
    return f"User {profile_id} has been deleted"

