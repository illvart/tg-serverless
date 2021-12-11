from os import path
from pathlib import Path

from envparse import env

# load environment variables from .env
app_dir: Path = Path(__file__).parent.parent
env_file = app_dir / ".env"
if path.isfile(env_file):
    env.read_envfile(env_file)

BOT_API_TOKEN = env.str("BOT_API_TOKEN", default="")
SERVERLESS = env.bool("SERVERLESS", default=False)
WEBHOOK_HOST = env.str("WEBHOOK_HOST", default="")
WEBAPP_HOST = env.str("HOST", default="0.0.0.0")
WEBAPP_PORT = env.int("PORT", default=3000)
