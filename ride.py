from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/requests', methods=['POST'])
def create_request():
    # create ride request logic
    ride_request = {'user_id': request.json['user_id'], 'driver_id': request.json['driver_id']}

    # save ride request to file
    with open('ride_requests.txt', 'a') as f:
        f.write(json.dumps(ride_request) + '\n')

    return json.dumps(ride_request)


@app.route('/requests/<int:request_id>', methods=['GET'])
def get_request(request_id):
    # get ride request logic
    ride_request = {'id': request_id, 'user_id': 1, 'driver_id': 1}

    return json.dumps(ride_request)


if __name__ == '__main__':
    app.run(debug=True)
