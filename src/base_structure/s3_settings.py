from ..constants import idap_bucket_project_code


class S3Settings:
    def __init__(self, stage):
        self.code_bucket = idap_bucket_project_code % stage
