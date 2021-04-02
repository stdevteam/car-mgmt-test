import logging
from logging.handlers import RotatingFileHandler
import pymysql
from flask import Flask

from .config import Config


db = pymysql.connect(
    user=Config.DATABASE_USER,
    password=Config.DATABASE_PASS,
    database=Config.DATABASE_NAME,
    host=Config.DATABASE_HOST,
    cursorclass=pymysql.cursors.DictCursor)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    handler = RotatingFileHandler('logging.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    app.logger.addHandler(handler)

    return app
