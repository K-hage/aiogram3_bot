from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent

if (env_path := BASE_DIR.joinpath('.env')) and env_path.is_file():
    env.read_envfile(env_path)

TOKEN = env.str('BOT_TOKEN')
ADMIN_ID = env.str('ADMIN_ID')
