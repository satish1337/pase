from .base import *
import os


if os.environ.get("ENV_NAME") == 'production':
    from .production import *
elif os.environ.get("ENV_NAME") == 'dev':
    from .dev import *
else:
    from .local import *