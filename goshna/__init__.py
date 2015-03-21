# This file is used to initialize global variables
# Like the Flask app and database cursor
from flask import Flask
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('goshna.sqlite', check_same_thread=False)
c = conn.cursor()
