import os

import json
import base64
import datetime

from db.models.Media import Media


def upload_media(media, user_email, user_id, collectionMedia):
    media_b64 = base64.b64encode(media.read())
    #decoded = base64.b64decode(media_b64)

    extension = get_extension(filename=media.filename)
    date = datetime.datetime.now()
    newMedia = Media(fileBase64=media_b64, extension=extension, user_email=user_email, user_id=user_id, created_at=date, updated_at=date)
    collectionMedia.insert_one(toJson(newMedia))

    return newMedia


def toJson(Media):
    print(Media.__dict__)
    
    return json.dumps((Media.__dict__).encode('utf-8'))

def get_extension(filename):
    parts = filename.rsplit(".")
    extension = parts[len(parts) - 1]

    if extension in os.getenv("ALLOWED_EXTENSION"):
        return extension

    return False