from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/drivers', methods=['POST'])
def create_driver():
    # create driver logic
    driver = {'name': request.json['name'], 'license': request.json['license']}

    # save driver to file
    with open('drivers.txt', 'a') as f:
        f.write(json.dumps(driver) + '\n')

    return json.dumps(driver)


@app.route('/drivers/<int:driver_id>', methods=['GET'])
def get_driver(driver_id):
    # get driver logic
    driver = {'id': driver_id, 'name': 'example', 'license': 'ABC123'}

    return json.dumps(driver)


if __name__ == '__main__':
    app.run(debug=True)
