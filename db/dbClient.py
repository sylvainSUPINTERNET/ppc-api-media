from conf import db
from pymongo import MongoClient


def get_connection(db_url=db.get_url_db()):
    return MongoClient(db_url)


