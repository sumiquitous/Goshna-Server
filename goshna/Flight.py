from flask import Flask, jsonify, abort, request
from goshna import *
from goshna import ApiFunctions, DisplayFlight
from datetime import date, time;

class Flight:
    def __init__(self, id, date, airline_id, source_airport_id, dest_airport_id, flight_number, departure_time):
        self.id = id
        self.date = date;
        self.airline_id = airline_id;
        self.source_airport_id = source_airport_id;
        self.dest_airport_id = dest_airport_id;
        self.flight_number = flight_number;
        self.departure_time = departure_time;

    def to_json(self):
        return {
            'id': self.id, 
            'date': self.date, 
            'airline_id': self.airline_id, 
            'source_airport_id': self.source_airport_id, 
            'dest_airport_id': self.dest_airport_id, 
            'flight_number': self.flight_number, 
            'departure_time': self.departure_time
        }

    @app.route('/goshna/api/flights', methods=['POST'])
    def create_flight():
        if not request.json or not 'airline_id' in request.json or not 'source_airport_id' in request.json or not 'dest_airport_id' in request.json or not 'flight_number' in request.json or not 'departure_time' in request.json or not 'date' in request.json:
            abort(400)

        date = request.json['date']
        airline_id = request.json['airline_id']
        source_airport_id = request.json['source_airport_id']
        dest_airport_id = request.json['dest_airport_id']
        flight_number = request.json['flight_number']
        departure_time = request.json['departure_time']

        result = ApiFunctions.post_db("INSERT INTO flights VALUES (NULL, ?, ?, ?, ?, ?, ?)", [date, airline_id, source_airport_id, dest_airport_id, flight_number, departure_time]);
        inserted_id = c.lastrowid

        print u'Inserted new flight at row ' + str(inserted_id)
        return jsonify({'id': str(inserted_id)}), 201

    @app.route('/goshna/api/flights/find', methods=['POST'])
    def find_flights():
        airline_id = 0
        airport_id = 0

        if request.json and 'airline_id' in request.json:
            airline_id = request.json['airline_id']

        if request.json and 'airport_id' in request.json:
            airport_id = request.json['airport_id']

        flights = []

        if(airline_id == 0):

            # Airport and Airline are 'ALL'
            if(airport_id == 0):
                results = ApiFunctions.query_db("SELECT * FROM flights", [])

            # Airline is 'ALL'
            else:
                results = ApiFunctions.query_db("SELECT * FROM flights where source_airport_id=?", [airport_id])

        # Airport is 'ALL'
        elif(airport_id == 0):
            results = ApiFunctions.query_db("SELECT * FROM flights where airline_id=?", [airline_id])

        # Neither is 'ALL'
        else:
            results = ApiFunctions.query_db("SELECT * FROM flights where airline_id=? and source_airport_id=?", [airline_id, airport_id])


        for row in results:
            airline = ApiFunctions.query_db("SELECT * FROM airlines WHERE id = ?", [row['airline_id']], one=True)
            dest_airport = ApiFunctions.query_db("SELECT * FROM airports WHERE id = ?", [row['dest_airport_id']], one=True)
            source_airport = ApiFunctions.query_db("SELECT * FROM airports WHERE id = ?", [row['source_airport_id']], one=True)

            flight = DisplayFlight.DisplayFlight(
                row['id'],
                row['date'],
                airline['airline_short'],
                source_airport['airport_short'],
                dest_airport['airport_short'],
                row['flight_number'],
                row['departure_time'],
                row['airline_id'],
                row['dest_airport_id'],
                row['source_airport_id']
            )

            flights.append(flight.to_json())

        return jsonify({'flights': flights})

    @app.route('/goshna/api/flights', methods=['GET'])
    def get_flights():
        flights = []
        results = ApiFunctions.query_db("SELECT * FROM flights")
        for row in results:
            flight = Flight(
                row['id'], 
                row['date'], 
                row['airline_id'], 
                row['source_airport_id'], 
                row['dest_airport_id'], 
                row['flight_number'], 
                row['departure_time']
            )

            flights.append(flight.to_json())

        return jsonify({'flights': flights})

	@app.route('/goshna/api/flights/<int:flight_id>', methods=['GET'])
	def get_flight(flight_id):

            row = ApiFunctions.query_db("SELECT * FROM flights WHERE id = ?", [flight_id], one=True)
            if row is None:
                abort(404)

            flight = Flight(
                row['id'], 
                row['date'], 
                row['airline_id'], 
                row['source_airport_id'], 
                row['dest_airport_id'], 
                row['flight_number'], 
                row['departure_time']
            )
            return jsonify({'flight': flight.to_json()})

	@app.route('/goshna/api/flights/<int:flight_id>', methods=['DELETE'])
	def delete_flight(flight_id):
            ApiFunctions.post_db("DELETE FROM flights WHERE id=?", [flight_id])
            print u'Deleted flight with ID ' + str(inserted_id)
            return jsonify({'result': True})
