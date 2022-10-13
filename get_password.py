import os
from dotenv import load_dotenv
from app.mongo_files.database import MongoDB


def get_password():
    load_dotenv()
    db = MongoDB()
    password = db.read(os.getenv("MONGO_COLLECTION"))[0][os.getenv("MONGO_FIELD")]
    print(password)


if __name__ == '__main__':
    get_password()
