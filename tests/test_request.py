# app/tests/v1/test_request.py

from app import create_app
import sys
import unittest
import json

class CreateRequestTestCase(unittest.TestCase):
    """
    Test class for testing if requests can be made 
    """
    def setUp(self):
        
        """
        Method hold data for tests before the tests run
        """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        self.list_request_empty ={}
        self.user = {
            "username":"mama", 
            "first_name":"Leeanne", 
            "last_name":"Khavai",
            "email": "leeann@maintenancetracker.com",
            "password": "Mama456",
            "confirm_password": "Mama456"
        }
        self.one_request = {
            "title":"Seat cannot bend",
            "description":"Seat not in a comfortable situation and need very super fast",
            "department":"Admin"
        } 
        self.two_request = {
            "title":"Site blocked",
            "description":"I cannot access this site , it says site blocked",
            "department": "IT Support"
        } 
        
        
    def test_user_can_make_a_request(self):
        """
        Test api if it can make a request
        """
        # Register a user first
        self.client().post('/maintenance_tracker/api/v1/auth/users',
                    data=json.dumps(self.user),
                    content_type='application/json')
        response = self.client().post('/maintenance_tracker/api/v1/requests',
                    data=json.dumps(self.one_request),
                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Request created successfully', str(response.data))
        
    def test_user_can_view_requests(self):
        """
        Test api can list all the requests
        """
        # Create a request
        self.client().post('/maintenance_tracker/api/v1/requests',
                    data=json.dumps(self.one_request),
                    content_type='application/json')
        # Test get request
        response = self.client().get('/maintenance_tracker/api/v1/requests',
                    content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_user_can_view_one_request(self):
        """
        Test api can show one request
        """
        # Create a request
        self.client().post('/maintenance_tracker/api/v1/requests',
                    data=json.dumps(self.one_request),
                    content_type='application/json')
        # Test get one request
        response = self.client().get('/maintenance_tracker/api/v1/requests/1',
                    content_type='application/json')
        self.assertEqual(response.status_code,200)
        
    def test_user_can_edit_a_request(self):
        """"
        Test api can edit a request
        """
        # Create a request
        edit_req = {
            "title":"CPU Failure",
            "description":"CPU cannot start",
            "department": "HR Department"
        }
        self.client().post('/maintenance_tracker/api/v1/requests',
                    data=json.dumps(edit_req),
                    content_type='application/json')
        edit_req["title"] = "Disfunctional mouse"
        edit_req["description"] = "Mouse not working"
        edit_req["department"] = "Finance"
        self.client().put('/maintenance_tracker/api/v1/requests/2',
                    data=json.dumps(edit_req),
                    content_type='application/json')
        self.assertEqual(edit_req['title'], "Disfunctional mouse")

    
    def test_delete_a_request(self):
        """
        Test api can delete an existing request
        """
        # Create request 1
        self.client().post('/maintenance_tracker/api/v1/requests', 
                                    data=json.dumps(self.one_request),
                                    content_type='application/json')
        # Create request 2
        self.client().post('/maintenance_tracker/api/v1/requests', 
                                    data=json.dumps(self.two_request),
                                    content_type='application/json')
        # Delete one_request
        response = self.client().delete('/maintenance_tracker/api/v1/requests/2', 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
if __name__=='__main__':
    unittest.main()