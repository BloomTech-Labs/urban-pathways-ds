from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from typing import List, Dict
from app.table_models import User, Awards, OneSiteData
from app.schema import SchemaUser, SchemaAwards, SchemaCreateOnesiteDB
from app.services import (get_db,
                          create_database,
                          read_awards,
                          save_awards_data,
                          save_onesite_data, read_onesite)

create_database()

app = FastAPI(
    title="Urban Pathways DS API",
    version="0.3.7",
    docs_url="/"
)


@app.get("/version/")
def version_endpoint():
    return {app.version}


@app.get("/read-awards/", response_model=List[SchemaAwards])
def read_users_endpoint(db: Session = Depends(get_db)):
    return read_awards(db=db)


@app.get("/read-onesite/", response_model=List[SchemaCreateOnesiteDB])
def read_onesite_endpoint(db: Session = Depends(get_db)):
    return read_onesite(db=db)


@app.post("/upload-awards-file")
def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Allows to upload files"""
    return save_awards_data(db=db, file=file)


@app.post("/upload-onesite-file")
async def onesite_upload_file_endpoint(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return save_onesite_data(db=db, file=file)


@app.delete("/nuke")
def nuke_endpoint(db: Session = Depends(get_db)):
    db.query(Awards).delete()
    db.query(OneSiteData).delete()
    db.commit()
    return "DataBase Nuked!"
