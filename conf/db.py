import os

def get_url_db():
    return os.getenv("URL_DB")

def init_db(client, db_name = os.getenv("DATABASE_NAME")):
    db = client[db_name]
    return db

def get_db_name():
    return os.getenv("DATABASE_NAME")

def init_collection(client, db, collection_name, db_name):
    return client[db_name][collection_name]
