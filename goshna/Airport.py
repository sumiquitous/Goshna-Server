from flask import Flask, jsonify, abort, request
from goshna import *
from goshna import ApiFunctions

class Airport:
    def __init__(self, id, name, code):
        self.id = id
        self.name = name
        self.code = code

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'code': self.code}

    @app.route('/goshna/api/airports', methods=['GET'])
    def get_airports():
        airports = []
        results = ApiFunctions.query_db("SELECT * FROM airports")
        for row in results:
            airport = Airport(row['id'], row['name'], row['code'])
            airports.append(airport.to_json())

        return jsonify({'airports': airports})

    @app.route('/goshna/api/airports/<int:airport_id>', methods=['GET'])
    def get_airport(airport_id):

        row = ApiFunctions.query_db("SELECT * FROM airports WHERE id = ?", [airport_id], one=True)
        if row is None:
            abort(404)

        airport = Airport(row['id'], row['name'], row['code'])
        return jsonify({'airport': airport.to_json()})

    @app.route('/goshna/api/airports', methods=['POST'])
    def create_airport():
        if not request.json or not 'code' in request.json or not 'name' in request.json:
            abort(400)
        
        name = request.json.get('name', '')
        code = request.json['code']
        result = ApiFunctions.post_db("INSERT INTO airports VALUES (NULL, ?, ?)", [name, code]);
        inserted_id = c.lastrowid
        airport = Airport(id, name, code)
        print u'Inserted new airport at row ' + str(inserted_id)
        return jsonify({'id': str(inserted_id)}), 201

    @app.route('/goshna/api/airports/<int:airport_id>', methods=['PUT'])
    def update_airport(airport_id):
        results = ApiFunctions.query_db("SELECT * FROM airports where id=?", [airport_id], one=True)
        if results is None:
            abort(404)
        if not request.json:
            abort(400)
        if 'name' in request.json and type(request.json['name']) != unicode:
            abort(400)
        if 'code' in request.json and type(request.json['code']) != unicode:
            abort(400)

        name = request.json['name']
        code = request.json['code']
        ApiFunctions.post_db("UPDATE airports SET name=?, code=? where id=?", [name, code, airport_id])

        airport = Airport(airport_id, name, code)
        return jsonify({'airport': airport.to_json()})

    @app.route('/goshna/api/airports/<int:airport_id>', methods=['DELETE'])
    def delete_airport(airport_id):
        ApiFunctions.post_db("DELETE FROM airports WHERE id=?", [airport_id])
        print u'Deleted airport with ID ' + str(inserted_id)
        return jsonify({'result': True})

