import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from conf import server, db
import base64

from services import media as service_media

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

#mydict = { "name": "Peter", "address": "Lowstreet 27" }
#x = collectionMedias.insert_one(mydict)
#print(x)
#for y in collectionMedias.find():
  #print(y)

@app.route(f"{server.get_prefix()}/")
def index():
    return jsonify({"db" : client.get_database()}), 200

@app.route(f"{server.get_prefix()}/medias", methods=["POST"])
def add_media():
    if 'media' not in request.files:
        return jsonify({"error": True, "message": "Media body is missing"}), 400
    if 'user_email' not in request.form:
        return jsonify({"error": True, "message": "user_email is missing"}), 400
    if 'user_id' not in request.form:
        return jsonify({"error": True, "message": "user_id is missing"}), 400

    media = request.files["media"]
    data = request.form

    extension = service_media.get_extension(filename=media.filename)

    if ( extension != False ) :
        service_media.upload_media(media=media, user_email=data["user_email"], user_id=data["user_id"], collectionMedia=collectionMedias)

        return jsonify({
            "error": False,
            "message": "Media uploaded successfully !"}), 200
    else :

        print(set(os.getenv("ALLOWED_EXTENSION")))
        allowed_extensions = " ".join([x for x in set(os.getenv("ALLOWED_EXTENSION")) ])
        print(allowed_extensions)
        return jsonify({
            "error": True,
            "message": allowed_extensions}), 400





@app.route(f"{server.get_prefix()}/medias", methods=["GET"])
def get_media():
    if 'media' not in request.files:
        return jsonify({"error": True, "message": "Media body is missing"}), 200

    media = request.files["media"]

    media_b64 = base64.b64encode(media.read())
    decoded = base64.b64decode(media_b64)
    return Response(decoded, mimetype="image/jpeg")