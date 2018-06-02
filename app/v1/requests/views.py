# app/v1/requests/views.py

from flask import Flask, request, jsonify, abort
from flask import make_response

from . import req
from app.v1.models import Request, User
from app.v1.auth.views import all_users

m_request = Request()
m_user = User()

# Create a request
@req.route('', methods=['POST'])
def add_request():
    data = request.get_json()
    if not request.json or not 'title' in request.json:
        abort(400)
    if len(all_users) == 0:
        return jsonify({"message": "No user exists. Register one first"})
    # Get the first user in the system
    if len(all_users.keys()) == 0:
        return jsonify({"message": "No user exists. Register one first"})
    first_user_key = list(all_users.keys())[0]
    first_user = all_users[first_user_key]
    user_id = first_user['user_id']
    req_id = len(m_request.requests) + 1
    new_request = {
        'id': req_id,
        'user_id': user_id,
        'title': data['title'],
        'description': data['description'],
        'department': data['department']
    }
    m_request.requests[req_id] = new_request
    return jsonify({'message': "Request created successfully"}), 201

# Get all requests
@req.route('', methods=['GET'])
def get_all_requests():
    return jsonify({'requests': m_request.requests})
    
# Get one request by ID 
@req.route('/<int:requestID>', methods=['GET'])
def get_single_request(requestID):
    error = []
    one_request = {}
    for one_req in m_request.requests.values():
        if one_req['id'] == requestID:
            one_request = one_req
        else:
            error.append({"Request does not exist"})
    if len(one_request) == 0:
        return jsonify({"error": error})
    return jsonify({"request": m_request.requests[requestID]})

# Edit a request
@req.route('/<int:requestID>', methods=['PUT'])
def edit_request(requestID):
    data = request.get_json()
    error = []
    one_request = {}
    for one_req in m_request.requests.values():
        if one_req['id'] == requestID:
            one_request = one_req
        else:
            error.append({"Request does not exist"})
    if len(one_request) == 0:
        return jsonify({"error": error})
    one_request['title'] = data['title']
    one_request['description'] = data['description']
    one_request['department'] = data['department']
    return jsonify({"message": "Request edited successfully"})

# Delete a request 
@req.route('/<int:requestID>', methods=['DELETE'])
def delete_request(requestID):
    error = []
    one_request = {}
    for one_req in m_request.requests.values():
        if one_req['id'] == requestID:
            one_request = one_req
        else:
            error.append({"Request does not exist"})
    if len(one_request) == 0:
        return jsonify({"error": error})
    del m_request.requests[requestID]
    return jsonify({"message": "Request deleted succesfully"})

