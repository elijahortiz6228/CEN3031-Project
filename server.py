from flask import Flask, redirect, url_for, request, jsonify, render_template
from flask_cors import CORS, cross_origin  # Import CORS

from login import register as reg
from login import login as log
import organizations as org
import profiles


# Dummy data to simulate user database
users = {
    'john@example.com': {
        'password': 'Password123!',
        'first_name': 'John',
        'last_name': 'Doe',
        'state': 'CA'
    }
}

# App
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}})



app = Flask(__name__)
CORS(app)  # Apply CORS to your Flask app

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')  # Safely retrieve email from data
    password = data.get('password')  # Safely retrieve password from data
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    state = data.get('state')
    name = f"{firstname} {lastname}"
    
    if reg(email, password, 'dog', firstname, lastname, state):
        profiles.createProfile(email, '', 'profile-pic.png')
        return jsonify({'message': 'Registration successful!', 'status': 200, 'token': email, 'name': name}), 200
    else:
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/registerOrg', methods=['POST'])
def registerOrg():
    data = request.get_json()
    password = data.get('password')
    email = data.get('email')
    name = data.get('name')
    phone = data.get('phone')
    addr = data.get('addr')
    orgType = data.get('orgType')
    bio = data.get('bio')
    if org.charity_register(name,email,password,phone,addr,orgType,bio):
        # Create Profile
        profiles.createOrgProfile(email, bio, 'profile-pic.png')
        # User authenticated, return success response
        return jsonify({'message': 'Registration successful!', 'status': 200, 'token': email, 'name':name}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if log(email,password):
        # User authenticated, return success response
        return jsonify({'message': 'Signin successful!', 'status': 200, 'token': profiles.getName(email), 'pfp':profiles.getPFP(email)}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/getProfile', methods=['POST'])
def getProfile():
    data = request.get_json()
    email = data.get('email')

    if profiles.getEntireProfile(email):
        ret = profiles.getEntireProfile(email)
        # User authenticated, return success response
        return jsonify({'message': 'Request successful!', 'status': 200, 'token': email, 'ret':ret}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    email = data.get('email')
    updateType = data.get('updateType')
    update = data.get('update')

    if updateType=='all':
        if profiles.update(email,update):
            # User authenticated, return success response
            return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
        else:
            # Incorrect email or password
            return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/updateFirstName', methods=['POST'])
def updateFirstName():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateFirstName(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/updateLastName', methods=['POST'])
def updateLastName():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateLastName(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

@app.route('/updateAddress', methods=['POST'])
def updateAddress():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateAddress(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/updateBio', methods=['POST'])
def updateBio():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updateBio(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401
    
@app.route('/updatePFP', methods=['POST'])
def updatePFP():
    data = request.get_json()
    email = data.get('email')
    update = data.get('update')

    if profiles.updatePFP(email,update):
        # User authenticated, return success response
        return jsonify({'message': 'Update successful!', 'status': 200, 'token': email}), 200
    else:
        # Incorrect email or password
        return jsonify({'error': 'Incorrect email or password'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5001)
