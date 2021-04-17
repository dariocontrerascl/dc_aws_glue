from aws_cdk import core
from .settings import Settings


def get_env(*, settings: Settings) -> core.Environment:
    return core.Environment(account=settings.account, region=settings.region)