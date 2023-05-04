from flask import Flask, jsonify, request
import user
import driver
import ride

app = Flask(__name__)

# Initialize microservices
user_management = user
driver_management = driver
ride_request = ride

# Define API routes
@app.route('/user', methods=['POST'])
def create_user():
    user = request.json
    user_management.create_user(user)
    return jsonify(user)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_management.get_user(user_id)
    return jsonify(user)

@app.route('/driver', methods=['POST'])
def create_driver():
    driver = request.json
    driver_management.create_driver(driver)
    return jsonify(driver)

@app.route('/driver/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = driver_management.get_driver(driver_id)
    return jsonify(driver)

@app.route('/ride_request', methods=['POST'])
def create_ride_request():
    ride = request.json
    ride_request.create_request(ride)
    return jsonify(ride)

@app.route('/ride_request/<int:ride_id>', methods=['GET'])
def get_ride_request(ride_id):
    ride = ride_request.get_request(ride_id)
    return jsonify(ride)

if __name__ == '__main__':
    app.run(debug=True)
