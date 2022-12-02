from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List, Dict
from app.table_models import OnepointUser, AwardsUser
from app.schema import SchemaOnePoint, SchemaAwards
from read_excel import read_xls, read_xlsx
from app.services import (get_db,
                          create_database,
                          create_user,
                          read_onepoint_users,
                          read_first,
                          update_user,
                          delete_user,
                          nuclear_launch_detected,
                          read_awards_users)

create_database()

app = FastAPI(
    title="Urban Pathways DS API",
    version="0.0.0",
    docs_url="/"
)


@app.get("/version/")
def version_endpoint():
    return {app.version}


@app.post("/create/user/", response_model=SchemaOnePoint)
def create_user_endpoint(user: SchemaOnePoint, db: Session = Depends(get_db)):
    user_check = read_first(db=db, profile_id=user.profile_id)
    if user_check:
        raise HTTPException(
            status_code=403,
            detail=f"Duplicate Entry, User {OnepointUser.profile_id} already exists"
        )
    else:
        return create_user(db=db, user=user)


@app.get("/read-onepoint-users/", response_model=List[SchemaOnePoint])
def read_onepoint_users_endpoint(db: Session = Depends(get_db)):
    return read_onepoint_users(db=db)


@app.get("/read-awards-users/", response_model=List[SchemaAwards])
def read_awards_users_endpoint(db: Session = Depends(get_db)):
    return read_awards_users(db=db)


@app.post("/read-workbook")
async def read_workbook(file: UploadFile):
    return {read_xls(file=file)}


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


@app.post("/populate/")
def populate_users_endpoint(file1: UploadFile = File(...),
                            file2: UploadFile = File(...),
                            db: Session = Depends(get_db)):
    if file1.filename[-4:] == ".xls":
        read_xls(file=file1, db=db)
        read_xlsx(file=file2, db=db)
    elif file1.filename[-4:] == "xlsx":
        read_xls(file=file2, db=db)
        read_xlsx(file=file1, db=db)


@app.delete("/nuke")
def nuke_db_endpoint(db: Session = Depends(get_db)):
    return nuclear_launch_detected(db=db)
