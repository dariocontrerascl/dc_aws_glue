from pydantic import BaseSettings, Field
from .constants import DEFAULT_CDK_ACCOUNT, DEFAULT_CDK_REGION


class Settings(BaseSettings):
    # Common settings
    account: str = Field(DEFAULT_CDK_ACCOUNT, name="124614996455")
    region: str = Field(DEFAULT_CDK_REGION, name="us-east-2")

