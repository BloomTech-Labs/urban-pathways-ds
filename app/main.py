from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from typing import List, Dict
from app.table_models import User, OneSiteData
from app.schema import SchemaUser, SchemaCreateOnesiteDB
from app.services import (get_db,
                          create_database,
                          create_user,
                          read_users,
                          read_first,
                          update_user,
                          delete_user,
                          save_onesite_data)


create_database()

app = FastAPI(
    title="Urban Pathways DS API",
    version="0.0.0",
    docs_url="/"
)


@app.get("/version/")
def version_endpoint():
    return {app.version}


@app.post("/create/user/", response_model=SchemaUser)
def create_user_endpoint(user: SchemaUser, db: Session = Depends(get_db)):
    user_check = read_first(db=db, profile_id=user.profile_id)
    if user_check:
        raise HTTPException(
            status_code=403,
            detail=f"Duplicate Entry, User {User.profile_id} already exists"
        )
    else:
        return create_user(db=db, user=user)


@app.get("/read-users/", response_model=List[SchemaUser])
def read_users_endpoint(db: Session = Depends(get_db)):
    return read_users(db=db)


@app.patch("/update/user/{profile_id}")
def update_users_endpoint(
        profile_id: str,
        update_data: Dict,
        db: Session = Depends(get_db)
):
    return update_user(profile_id=profile_id, update_data=update_data, db=db)


@app.delete("/delete/user/{profile_id}")
def delete_user_endpoint(profile_id: str, db: Session = Depends(get_db)):
    return delete_user(db=db, profile_id=profile_id)


@app.post("/upload/onesite/data/") 
def create_onesite_endpoint(file: UploadFile = File(...), db: Session = Depends(get_db)): 
    return save_onesite_data(db, file)
