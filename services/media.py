import os

def upload_media():
    return "ok"


def get_extension(filename):
    parts = filename.rsplit(".")
    extension = parts[len(parts) - 1]

    if extension in os.getenv("ALLOWED_EXTENSION"):
        return extension

    return False