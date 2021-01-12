import os

import uuid
import arrow
import json
import base64
import uuid


from db.models.Media import Media


# TODO => https://www.naun.org/multimedia/NAUN/computers/20-462.pdf => algo for explicit pictures to integrate later
def upload_media(media, user_email, user_id, collectionMedia):
    media_b64 = base64.b64encode(media.read()) # byte
    media_b64_str = media_b64.decode("utf-8")
    #decoded = base64.b64decode(media_b64)

    extension = get_extension(filename=media.filename)
    now = arrow.utcnow().format('YYYY-MM-DDTHH:mm:ss.SSS')
    generated_uuid = uuid.uuid4()

    newMedia = Media(file_base_64=media_b64_str, extension=extension, user_email=user_email, user_id=user_id, uuid=str(generated_uuid),created_at=now, updated_at=now)
    collectionMedia.insert_one(newMedia.__dict__)

    return newMedia

def get_media(media_uuid, collectionMedia):
    target_media = collectionMedia.find_one({"uuid": media_uuid})
    return target_media

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
