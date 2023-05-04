from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def create_user():
    # create user logic
    user = {'username': request.json['username'], 'email': request.json['email']}

    # save user to file
    with open('users.txt', 'a') as f:
        f.write(json.dumps(user) + '\n')

    return json.dumps(user)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # get user logic
    user = {'id': user_id, 'username': 'exampleUser', 'email': 'example@mail.com'}

    return json.dumps(user)


if __name__ == '__main__':
    app.run(debug=True)
