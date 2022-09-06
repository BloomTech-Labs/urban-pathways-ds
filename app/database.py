""" MongoDB Interface """
from os import getenv
from typing import Optional, List, Dict, Iterable

from pymongo import MongoClient
from pymongo.collection import Collection
from dotenv import load_dotenv


class MongoDB:
    """ DocTests
    >>> db = MongoDB()
    >>> db.create({"Test": True})
    True
    >>> db.read({"Test": True})
    [{'Test': True}]
    >>> db.update({"Test": True}, {"New Field": True})
    True
    >>> db.read({"Test": True})
    [{'Test': True, 'New Field': True}]
    >>> db.delete({"Test": True})
    True
    >>> db.read({"Test": True})
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
