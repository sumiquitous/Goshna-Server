from flask import Flask, jsonify, abort, request
from goshna import *
from goshna import ApiFunctions

class User:
    def __init__(self, id):
        self.id = id

    def to_json(self):
        return {'id': self.id}

    @app.route('/goshna/api/users', methods=['GET'])
    def get_users():
        users = []
        results = ApiFunctions.query_db("SELECT * FROM users")
        for row in results:
            user = User(row['id'])
            users.append(user.to_json())

        return jsonify({'users': users})

    @app.route('/goshna/api/user', methods=['POST'])
    def create_user():
        result = ApiFunctions.post_db("INSERT INTO users VALUES (NULL)");
        inserted_id = c.lastrowid
        user = User(id)
        print u'Inserted new user at row ' + str(inserted_id)
        return jsonify({'id': str(inserted_id)}), 201

    @app.route('/goshna/api/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        ApiFunctions.post_db("DELETE FROM users WHERE id=?", [user_id])
        print u'Deleted user with ID ' + str(inserted_id)
        return jsonify({'result': True})

