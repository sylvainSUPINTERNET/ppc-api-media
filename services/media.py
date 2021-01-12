import os

import uuid
import arrow
import json
import base64
import uuid


from db.models.Media import Media


def upload_media(media, user_email, user_id, collectionMedia):
    media_b64 = base64.b64encode(media.read()) # byte
    media_b64_str = media_b64.decode("utf-8")
    #decoded = base64.b64decode(media_b64)

    extension = get_extension(filename=media.filename)
    now = arrow.utcnow().format('YYYY-MM-DDTHH:mm:ss.SSS')
    generated_uuid = uuid.uuid4()

    newMedia = Media(fileBase64=media_b64_str, extension=extension, user_email=user_email, user_id=user_id, uuid=str(generated_uuid),created_at=now, updated_at=now)
    collectionMedia.insert_one(newMedia.__dict__)

    return newMedia


def toJson(Media):
    print(Media.__dict__)
    return json.dumps((Media.__dict__))

def get_extension(filename):
    parts = filename.rsplit(".")
    extension = parts[len(parts) - 1]

    if extension in os.getenv("ALLOWED_EXTENSION"):
        return extension

    return False


def get_media_name(filename):
    parts = filename.rsplit(".")
    extension = parts[len(parts) - 1]

    if extension in os.getenv("ALLOWED_EXTENSION"):
        return extension

    return False
