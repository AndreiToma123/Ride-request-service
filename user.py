from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379)

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

def create_user(name, email):
    id = redis_client.incr('user_id')
    user = User(id, name, email)
    user_data = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }
    redis_client.hmset(f'user:{user.id}', user_data)
    return user.id

def get_user(id):
    user_data = redis_client.hgetall(f'user:{id}')
    if not user_data:
        return None
    user = User(user_data[b'id'], user_data[b'name'], user_data[b'email'])
    return user


@app.route('/users', methods=['POST'])
def create_user_api():
    data = request.json
    name = data['name']
    email = data['email']
    user_id = create_user(name, email)
    return jsonify({'id': user_id})

@app.route('/users/<int:id>', methods=['GET'])
def get_user_api(id):
    user = get_user(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email
    })

