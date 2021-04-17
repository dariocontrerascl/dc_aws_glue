from aws_cdk import core
from .env import get_env
from .glue import glue
from .settings import Settings


def create_app(*, settings: Settings = None) -> core.App:
    if settings is None:
        settings = Settings()

    env = get_env(settings=settings)
    app = core.App()
    print(1, env)
    glue.GlueStack(app, settings=settings, env=env)
    return app