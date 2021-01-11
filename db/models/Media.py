import datetime

class Media :
    fileBase64 = ""
    extension = ""
    created_at = ""
    updated_at = ""
    user_email=""
    user_id=""

    def __init__(self, fileBase64, extension, user_email, user_id, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()):
        self.fileBase64 = fileBase64
        self.extension = extension
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_email = user_email
        self.user_id = user_id
