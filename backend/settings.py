# coding: UTF-8
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


DB = MySQLDatabase(
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    host=os.environ.get('DB_HOST'),
    port=int(os.environ.get('DB_PORT'))
)

FLASK_PORT = int(os.environ.get('FLASK_PORT'))
