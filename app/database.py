from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()
engine = create_engine(
    url=os.getenv("SQL_DB_URL", default="sqlite:///:memory:"),
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
