from flask import Flask, jsonify
from flask_cors import CORS
from conf import server, db

from db import dbClient

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
cors = CORS(app, resources={r"/v1/api/*": {"origins": "*"}})

# Init DB
client = dbClient.get_connection()
database = db.init_db(client)
print(client.list_database_names())

# Init collections
collectionMedias = db.init_collection(client, database, "medias", db.get_db_name())
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = collectionMedias.insert_one(mydict)
print(x)

for y in collectionMedias.find():
  print(y)

@app.route(f"{server.get_prefix()}/")
def index():
    return jsonify({"db" : client.get_database()}), 200