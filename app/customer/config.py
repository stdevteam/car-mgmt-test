import os

basedir = os.path.abspath(os.path.dirname(__file__))

# We can easily create development and production configs from this then.
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = True
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'db_name')
    DATABASE_USER = os.getenv('DATABASE_USER', 'db_user')
    DATABASE_HOST = os.getenv('DATABASE_HOST', '127.0.0.1')
    DATABASE_PASS = os.getenv('DATABASE_PASS', 'db_pass')


key = Config.SECRET_KEY
