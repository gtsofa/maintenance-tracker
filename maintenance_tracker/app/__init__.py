# app/__init__.py

from flask import Flask, jsonify

# initialize the app

app = Flask(__name__)

# create a memory database of requests .. a simply array of dictionaries
list_requests = [
    {
        'id': 1,
        "title":"Site blocked",
        "description":"I cannot access this site , it says site blocked",
        "department": "IT Support",
    },
    {
        'id': 2,
        "title":"Seat cannot bend back",
        "description":"This seat is very uncomfortable when you try to lean behind it doesn't work. ",
        "department": "Admin",
    }
    
    ]
   
 # View all requests from list_requests 
@app.route('/maintenance_tracker/api/v1/requests', methods=['GET'])
def get_all_requests():
    return jsonify({'list_requests': list_requests})
    
# View 1 single request using the requestID
@app.route('/maintenance_tracker/api/v1/requests/<int:requestID>', methods=['GET'])
def get_single_request(requestID):
    list_request = [list_request for list_request in list_requests if list_request['id'] == requestID]
    if len(list_request) == 0:
        abort(404)
    return jsonify({'list_request': list_request[0]})
    
# Add a new request to the database 
@app.route('/maintenance_tracker/api/v1/requests/<int:requestID>', methods=['POST'])
def add_request(request):
    if not request.json or not 'title' in request.json:
        abort(400)
        
    list_request = {
        'id': list_requests[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'department': False
    }
    list_requests.append(list_request)
    return jsonify({'list_request': list_request}), 201
        
    
if __name__=='__main__':
    app.run(debug=True)