from aws_cdk import core

from .constants import STAGES
from .env import get_env
from .glue import glue
from .settings import Settings


def create_app(*, settings: Settings = None) -> core.App:
    if settings is None:
        settings = Settings()

    env = get_env(settings=settings)
    app = core.App()
    for stage in STAGES:
        glue.GlueStack(app, settings=settings, stage=str(stage), env=env)
    return app
