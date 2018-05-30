# app/tests/v1/test_request.py

from app import app
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
        app.testing = True
        self.app = app.test.client
        
        
    def test_user_can_make_a_request(self):
        """
        Test api if it can make a requests
        """
        new_request = {
            "title":"Seat cannot bend",
            "description":"Seat not in a comfortable situation and need very super fast",
            "department":"Admin"
        }
        response = self.app.post('/api/v1/auth/request',
                    data=json.dumps(new_request,
                    content_type='application/json'))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Request created successfully', str(response.data))
        
    def test_user_can_view_request(self):
        """
        Test api can list all the requests
        """
        new_request = {
            "title":"Seat cannot bend",
            "description":"Seat not in a comfortable situation and need very super fast",
            "department":"Admin"
        }
        response = self.app.get('api/v1/auth/request/1',
                    data=json.dumps(new_request),
                    content_type='application/json')
        self.assertEqual(response.status_code,200)
        
    def test_user_can_edit_a_request(self):
        """"
        Test api can edit a request
        """
        updated_request = {
            "title":"Site blcoked",
            "description":"Check my site is blocked and i cannot work on it. Seat not in a comfortable situation and need very super fast",
            "department":"IT support"
        }
        response = self.app.put('api/v1/auth/request/1',
                    data=updated_request)
        self.assertEqual(response.status_code,200)
        
        
if __name__=='__main__':
    unittest.main()
		
		