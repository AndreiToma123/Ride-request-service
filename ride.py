from flask import Flask, jsonify, request
import redis
import uuid
import json

app = Flask(__name__)
cache = redis.Redis(host='localhost', port=6379)

@app.route('/ride_request', methods=['POST'])
def request_ride():
    # Generate a unique ride ID
    ride_id = str(uuid.uuid4())

    # Get ride request data from the request
    data = request.json
    user_id = data['user_id']
    start_location = data['start_location']
    end_location = data['end_location']
    ride_type = data['ride_type']

    # Cache the ride request data
    ride_data = {
        'user_id': user_id,
        'start_location': start_location,
        'end_location': end_location,
        'ride_type': ride_type
    }
    cache.set(ride_id, json.dumps(ride_data))

    # Return the ride ID to the user
    return jsonify({'ride_id': ride_id})

@app.route('/ride_request/<ride_id>', methods=['GET'])
def get_ride_request(ride_id):
    # Get the ride request data from the cache
    ride_data = cache.get(ride_id)
    if ride_data is None:
        return jsonify({'error': 'Ride request not found'}), 404

    # Return the ride request data to the user
    return jsonify(json.loads(ride_data))

if __name__ == '__main__':
    app.run(debug=True)
