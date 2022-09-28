""" MongoDB Interface """
from os import getenv
from typing import Optional, List, Dict, Iterable

from pymongo import MongoClient
from pymongo.collection import Collection
from dotenv import load_dotenv

from app.mongo_files.validation import default_user


class MongoDB:
    """ DocTests
    >>> db = MongoDB()
    >>> db.create("Users", default_user)
    True
    >>> db.read("Users")
    [{'name': 'John Smith', 'age': 42, 'email': 'john.smith@gmail.com', 'active': False, 'score': 0.5}]
    >>> db.update("Users", {'name': 'John Smith'}, {'name': 'Tony Smith'})
    True
    >>> db.read("Users")
    [{'name': 'Tony Smith', 'age': 42, 'email': 'john.smith@gmail.com', 'active': False, 'score': 0.5}]
    >>> db.delete("Users", {'name': 'Tony Smith'})
    True
    >>> db.read("Users")
    []
    """
    load_dotenv()

    def collection(self, collection: str) -> Collection:
        """ Connects to the MongoDB Collection
        @return: Collection """
        return MongoClient(
            getenv("MONGO_URL")
        )[getenv("MONGO_DB")][collection]

    def create(self, collection: str, data: Dict) -> bool:
        """ Creates one record in the Collection
        @param collection: str
        @param data: Dict
        @return: Boolean Success """
        return self.collection(collection).insert_one(dict(data)).acknowledged

    def create_many(self, collection: str, data: Iterable[Dict]) -> bool:
        """ Creates many records in the Collection
        @param collection: str
        @param data: Iterable[Dict]
        @return: Boolean Success """
        return self.collection(collection).insert_many(map(dict, data)).acknowledged

    def read(self, collection: str, query: Optional[Dict] = None) -> List[Dict]:
        """ Returns a list of records from the collection
        @param collection: str
        @param query: Dict
        @return: List[Dict] """
        return list(self.collection(collection).find(query, {"_id": False}))

    def update(self, collection: str, query: Dict, update_data: Dict) -> bool:
        """ Updates the matched records with new data
        @param collection: str
        @param query: Dict
        @param update_data: Dict
        @return: Boolean Success """
        return self.collection(collection).update_many(
            query, {"$set": update_data}
        ).acknowledged

    def delete(self, collection: str, query: Dict) -> bool:
        """ Deletes the matched records
        @param collection: str
        @param query: Dict
        @return: Boolean Success """
        return self.collection(collection).delete_many(query).acknowledged
