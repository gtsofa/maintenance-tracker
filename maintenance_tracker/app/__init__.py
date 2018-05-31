# app/__init__.py

from flask import Flask, jsonify, request, abort

# initialize the app

app = Flask(__name__)

# create a memory database of requests .. a simply array of dictionaries
list_requests = []

 # GET all VIEW all 
@app.route('/maintenance_tracker/api/v1/requests', methods=['GET'])
def get_all_requests():
    return jsonify({'list_requests': list_requests})
    
# GET 1 
@app.route('/maintenance_tracker/api/v1/requests/<int:requestID>', methods=['GET'])
def get_single_request(requestID):
    list_request = [list_request for list_request in list_requests if list_request['id'] == requestID]
    if len(list_request) == 0:
        abort(404)
    return jsonify({'list_request': list_request[0]})
    
# POST
@app.route('/maintenance_tracker/api/v1/requests', methods=['POST'])
def add_request():
    if not request.json or not 'title' in request.json:
        abort(400)
        
    list_request = {
        'id': len(list_requests) + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'department': request.json['department']
    }
    list_requests.append(list_request)
    return jsonify({'list_request': list_request}), 201

# PUT
@app.route('/maintenance_tracker/api/v1/requests/<int:requestID>', methods=['PUT'])
def edit_request(requestID):
    list_request = [list_request for list_request in list_requests if list_request['id']== requestID]
    if len(list_request) == 0:
        abort(404)
    if not request.json:
        abort(400)
    list_request[0]['title'] = request.json.get('title', list_request[0]['title'])
    list_request[0]['description'] = request.json.get('description', list_request[0]['description'])
    list_request[0]['department'] = request.json.get('department', list_request[0]['department'])
    return jsonify({'list_request': list_request[0]})

# DELETE 
@app.route('/maintenance_tracker/api/v1/requests/<int:requestID>', methods=['DELETE'])
def delete_request(requestID):
    list_request = [list_request for list_request in list_requests if list_request['id'] == requestID]
    if len(list_request) == 0:
        abort(404)
    list_requests.remove(list_request[0])
    return jsonify({'result': True})




        
    
if __name__== '__main__':
    app.run(debug=True)