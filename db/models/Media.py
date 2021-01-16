import arrow

class Media :
    file_base_64 = ""
    extension = ""
    created_at = ""
    updated_at = ""
    user_email=""
    user_uuid=""
    uuid = ""

    def __init__(self, file_base_64, extension, user_email, user_uuid, uuid,created_at=arrow.utcnow().format('YYYY-MM-DDTHH:mm:ss.SSS'), updated_at=arrow.utcnow().format('YYYY-MM-DDTHH:mm:ss.SSS')):
        self.file_base_64 = file_base_64
        self.extension = extension
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_email = user_email
        self.user_uuid = user_uuid,
        self.uuid = uuid
