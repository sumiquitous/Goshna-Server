from flask import Flask, jsonify, abort, request
from goshna import *
from goshna import ApiFunctions

class ListeningUser:
    def __init__(self, user_id, flight_id):
        self.user_id = user_id
        self.flight_id = flight_id

    def to_json(self):
        return {'user_id': self.user_id, 'flight_id': self.flight_id}

    @app.route('/goshna/api/listening_users', methods=['GET'])
    def get_listening_users():
        listening_users = []
        results = ApiFunctions.query_db("SELECT * FROM listening_users")
        for row in results:
            listening_user = ListeningUser(row['user_id'], row['flight_id'])
            listening_users.append(listening_user.to_json())

        return jsonify({'listening_users': listening_users})

    @app.route('/goshna/api/listening_users', methods=['POST'])
    def create_listening_user():
        if not request.json or not 'userid' in request.json or not 'flightid' in request.json:
            abort(400)
        
        user_id = request.json['userid']
        flight_id = request.json['flightid']
        result = ApiFunctions.post_db("INSERT INTO listening_users VALUES (?, ?)", [user_id, flight_id]);
        inserted_id = c.lastrowid
        print u'Inserted new listening_user at row ' + str(inserted_id)
        return jsonify({'id': str(inserted_id)}), 201

    @app.route('/goshna/api/listening_users/<int:listening_user_id>', methods=['DELETE'])
    def delete_listening_user(listening_user_id):
        ApiFunctions.post_db("DELETE FROM listening_users WHERE user_id=? and flight_id=?", [user_id, flight_id])
        print u'Deleted listening_user with ID ' + str(inserted_id)
        return jsonify({'result': True})

