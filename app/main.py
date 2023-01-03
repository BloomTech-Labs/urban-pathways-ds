from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from app.table_models import User
from app.services import (get_db,
                          create_database,
                          read_users,
                          read_first,)

app = FastAPI(
    title="Urban Pathways DS API",
    version="0.0.0",
    docs_url="/"
)

create_database()


@app.get("/version/")
def version_endpoint():
    return {app.version}

@app.get("/read-users/", response_model=List[SchemaUser])
def read_users_endpoint(db: Session = Depends(get_db)):
    return read_users(db=db)
