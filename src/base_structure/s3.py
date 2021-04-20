from typing import Any
from aws_cdk import core, aws_s3
from ..settings import Settings
from .s3_settings import S3Settings


class S3Stack(core.Stack):
    def __init__(self, scope: core.Construct, *, settings: Settings, stage: str, **kwargs: Any, ) -> None:
        ID_STACK = "idap-%s-s3-reporting" % stage
        super().__init__(scope, ID_STACK, **kwargs)
        self.settings = settings
        self.stage = stage
        self.s3_settings = S3Settings(self.stage)

        aws_s3.Bucket(self, self.s3_settings.code_bucket, bucket_name=self.s3_settings.code_bucket)
