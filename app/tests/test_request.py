# app/tests/v1/test_request.py

from app import app
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
        self.app = app
        self.client = self.app.test_client

        self.list_request_empty ={}

        self.list_request = {

            "title":"Seat cannot bend",
            "description":"Seat not in a comfortable situation and need very super fast",
            "department":"Admin"
        } 
        
        
    def test_user_can_make_a_request(self):
        """
        Test api if it can make a request
        """
        response = self.app.post('/maintenance_tracker/api/v1/requests',
                    data=json.dumps(self.list_request,
                    content_type='application/json'))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Request created successfully', str(response.data))
        
    def test_user_can_view_requests(self):
        """
        Test api can list all the requests
        """
        response = self.app.get('/maintenance_tracker/api/v1/requests',
                    data=json.dumps(self.list_request),
                    content_type='application/json')
        self.assertEqual(response.status_code,200)
        
    def test_user_can_edit_a_request(self):
        """"
        Test api can edit a request
        """
        response = self.app.put('/maintenance_tracker/api/v1/requests/1',
                    data=self.list_request)
        self.assertEqual(response.status_code,200)

    def test_if_can_create_empty_request(self):
        """
        Test api return an empty dictionary if  empty request
        """
        response = self.client().post('/maintenance_tracker/api/v1/requests', 
                        data=json.dumps(self.list_request_empty),
                        content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_delete_a_request(self):
        """
        Test api can delete an existing request
        """
        response = self.client().post('/maintenance_tracker/api/v1/requests', 
                                    data=json.dumps(self.list_request),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        json_result = json.loads(response.data.decode())
        response = self.client().delete('/maintenance_tracker/api/v1/requests/{}'.format(json_result))
        response = self.client().get('/maintenance_tracker/api/v1/requests/{}'.format(json_result))
        self.assertEqual(response.status_code, 404)

    def test_delete_a_request_that_do_not_exist(self):
        """
        Test api can delete a request that doesn't exist
        """
        response = self.client().delete('/maintenance_tracker/api/v1/requests/{}')
        self.assertEqual(response.status_code, 404)


        
        
if __name__=='__main__':
    unittest.main()
		
		