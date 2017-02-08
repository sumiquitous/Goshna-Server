# This file is used to initialize global variables
# Like the Flask app and database cursor
from flask import Flask
from flask_cors import CORS, cross_origin
import sqlite3

app = Flask(__name__)
CORS(app)
conn = sqlite3.connect('goshna.sqlite', check_same_thread=False)
c = conn.cursor()

# Flights
#c.execute('''drop table flights''')
#c.execute('''drop table messages''')
#c.execute('''drop table airlines''')
#c.execute('''drop table airports''')
#c.execute('''drop table users''')
#c.execute('''drop table listening_users''')
#c.execute('''drop table gates''')
#c.execute('''drop table flight_gates''')
#
#c.execute('''create table flights(id integer primary key autoincrement, date text, airline_id int, source_airport_id int, dest_airport_id int, flight_number int, departure_time text)''')
#
## Messages
#c.execute('''create table messages(id integer primary key autoincrement, text text, time int, flight_id int)''')
#
## Airlines
#c.execute('''create table airlines(id integer primary key autoincrement, airline_short text, airline_full text)''')
#
## Airports
#c.execute('''create table airports(id integer primary key autoincrement, airport_short text, airport_full text)''')
#
## Users
#c.execute('''create table users(id integer primary key autoincrement)''')
#
## ListeningUsers
#c.execute('''create table listening_users(user_id int, flight_id int)''')

## Gates
#c.execute('''create table gates(id integer primary key autoincrement, name text, airport_id int)''')

## FlightGates
#c.execute('''create table flight_gates(id integer primary key autoincrement, flight_id int, gate_id int)''')

conn.commit()
