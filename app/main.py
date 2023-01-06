from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from typing import List, Dict
from app.table_models import User, Awards
from app.schema import SchemaUser, SchemaAwards
from app.services import (get_db,
                          create_database,
                          read_awards,
                          save_awards_data)

create_database()

app = FastAPI(
    title="Urban Pathways DS API",
    version="0.0.0",
    docs_url="/"
)


@app.get("/version/")
def version_endpoint():
    return {app.version}


@app.get("/read-awards/", response_model=List[SchemaAwards])
def read_users_endpoint(db: Session = Depends(get_db)):
    return read_awards(db=db)


@app.post("/upload-awards-file")
def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Allows to upload files"""
    return save_awards_data(db, file)

