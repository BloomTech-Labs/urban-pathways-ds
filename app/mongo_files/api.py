import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from app.mongo_files.database import MongoDB
from app.mongo_files.validation import User, UserQuery, UserUpdate
from app.mongo_files.validation import default_query, default_update, default_user


API = FastAPI(
    title="Urban Pathways DS API",
    version="0.0.2",
    docs_url="/",
)

API.db = MongoDB()

API.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@API.get("/version")
async def api_version():
    """ Returns current API version
    @return: String Version """
    local = os.getenv("CONTEXT") == "local"
    remote = "Please run API locally using the correct environment variables"
    password = API.db.read("Secret")[0]["Password"] if local else remote
    return {"Version": API.version, "Password": password}


@API.post("/create-user")
async def create_user(user: User = default_user):
    """ Creates one user
    @param user: User
    @return: Boolean Success """
    return API.db.create("Users", user.dict(exclude_none=True))


@API.put("/read-users")
async def read_users(user_query: UserQuery = default_query):
    """ Returns array of all matched users
    @param user_query: UserQuery
    @return: Array[User] """
    return API.db.read("Users", user_query.dict(exclude_none=True))


@API.patch("/update-users")
async def update_users(user_query: UserQuery = default_query,
                       user_update: UserUpdate = default_update):
    """ Updates all matched users
    @param user_query: UserQuery
    @param user_update: UserUpdate
    @return: Boolean Success """
    return API.db.update(
        "Users",
        user_query.dict(exclude_none=True),
        user_update.dict(exclude_none=True),
    )


@API.delete("/delete-users")
async def delete_users(user_query: UserQuery = default_query):
    """ Deletes all matched users
    @param user_query: UserQuery
    @return: Boolean Success """
    return API.db.delete("Users", user_query.dict(exclude_none=True))
