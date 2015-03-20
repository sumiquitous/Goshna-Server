#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

airports = [
    {
        'id':   1,
        'name': u'Tampa International Airport',
        'code': u'TIA'
    },
    {
        'id':   2,
        'name': u'Miami International Airport',
        'code': u'MIA'
    },
    {
        'id':   3,
        'name': u'Orlando International Airport',
        'code': u'ORL'
    },
]

@app.route('/goshna/api/airports', methods=['GET'])
def get_airports():
    return jsonify({'airports': airports})

@app.route('/goshna/api/airports', methods=['POST'])
def create_airport():
    if not request.json or not 'code' in request.json:
        abort(400)
    airport = {
        'id': airports[-1]['id'] + 1,
        'name': request.json.get('name', ''),
        'code': request.json['code']
    }
    airports.append(airport)
    return jsonify({'airport': airport}), 201

@app.route('/goshna/api/airports/<int:airport_id>', methods=['GET'])
def get_airport(airport_id):
    airport = [airport for airport in airports if airport['id'] == airport_id]
    if len(airport) == 0:
        abort(404)
    return jsonify({'airport': airport[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
