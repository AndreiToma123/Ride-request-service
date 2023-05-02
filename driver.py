from flask import Flask, jsonify, request
import redis
import json

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# Driver Model
class Driver:
    def __init__(self, id, name, car_model, car_license_plate):
        self.id = id
        self.name = name
        self.car_model = car_model
        self.car_license_plate = car_license_plate

# API Routes
@app.route('/drivers', methods=['POST'])
def add_driver():
    id = request.json['driver_id']
    name = request.json['name']
    car_model = request.json['car_model']
    car_license_plate = request.json['car_license_plate']
    driver = Driver(id, name, car_model, car_license_plate)
    cache.set('driver:' + id, json.dumps(driver.__dict__))
    return jsonify({'driver': driver.__dict__})


@app.route('/drivers/<string:driver_id>', methods=['GET'])
def get_driver(id):
    driver = json.loads(cache.get('driver:' + id))
    return jsonify({'driver': driver})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
