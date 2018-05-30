# app/v1/requests/views.py

from flask import Flask,request,jsonify,abort
from flask import make_response

list_requests = []
@req.route('maintenance_tracker/api/v1/requests', methods=['POST'])
def post_requests():
    if not 'title' in request.json:
        abort(400)
        api_request = {
            'id':request.json['id'],
            'title': request.json['title'],
            'description': request.json['description'],
            'department': request.json['department']
        }
        list_requests.append(api_request)

    return jsonify({'api_request': list_requests}),201

#Get requests
@req.route('maintenance_tracker/api/v1/requests', methods=['GET'])
def get_all_requests():
    return jsonify({'requests':list_requests})

# Get a single request using ID
@req.route('maintenance_tracker/api/v1/requests/<int:requestID>', methods=['GET'])
def get_request(requestID):
    for request in requests:
        if request['id'] == requestID:

            if len(request) == 0:
                abort(404)
            return jsonify({'request': request[0]})

# Edit a request
@req.route('maintenance_tracker/api/v1/requests/<int:requestID>', methods=['PUT'])
def edit_request(requestID):
    edit_request = [request for request in requests if request['id']==requestID]
    if len(update_request) == 0:
			abort(404)

    update_request[0]['title'] = request.json.get('title', update_request[0]['title'])
		update_request[0]['description'] = request.json.get('description', update_request[0]['description'])
		update_request[0]['department'] = request.json.get('department', update_request[0]['department'])
		return jsonify({'update_request': edit_request[0]})	


