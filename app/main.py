from fastapi import FastAPI, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from app.schema import SchemaOneSite, SchemaAwards
from read_excel import read_xls, read_xlsx
from app.services import (get_db,
                          create_database,
                          read_onesite_users,
                          nuclear_launch_detected,
                          read_awards_users,)

create_database()

app = FastAPI(
    title="Urban Pathways DS API",
    version="0.0.0",
    docs_url="/"
)


@app.get("/version/")
def version_endpoint():
    return {app.version}


@app.get("/read-onesite-users/", response_model=List[SchemaOneSite])
def read_onesite_users_endpoint(db: Session = Depends(get_db)):
    return read_onesite_users(db=db)


@app.get("/read-awards-users/", response_model=List[SchemaAwards])
def read_awards_users_endpoint(db: Session = Depends(get_db)):
    return read_awards_users(db=db)


@app.post("/upload-onesite-data")
async def upload_onesite_data_endpoint(
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    return read_xls(db=db, file=file)


@app.post("/upload-awards-data")
async def upload_awards_data_endpoint(
        db: Session = Depends(get_db),
        file: UploadFile = File(...)
):
    return read_xlsx(db=db, file=file)


@app.delete("/nuke")
async def nuke_db_endpoint(db: Session = Depends(get_db)):
    return nuclear_launch_detected(db=db)
