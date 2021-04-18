from pydantic import BaseSettings, Field
from .constants import DEFAULT_CDK_ACCOUNT, DEFAULT_CDK_REGION


class Settings(BaseSettings):
    # Common settings
    account: str = Field(DEFAULT_CDK_ACCOUNT, env="DEFAULT_CDK_ACCOUNT", name="DEFAULT_CDK_ACCOUNT")
    region: str = Field(DEFAULT_CDK_REGION, env="DEFAULT_CDK_REGION", name="DEFAULT_CDK_REGION")

