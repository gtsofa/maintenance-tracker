# app/tests/test_user.py

import sys
import unittest
import json
from views import app

class CreateUserTestCase(unittest.TestCase):
    """
    This class tests the User 
    """
    def setUp(self):
        """
        This method will be called before every time a test runs, 
        and will create data for use by the tests
        """
        self.app = app
        self.client = self.app.test_client

        self.user = {
            "username":"maestro",
            "name":"Maestro Tsofa",
            "email":"maestro@maintenance_tracker.com",
            "password":"amka123"
        }

    def tearDown(self):
        """
        This method will be called after the tests run. 
        It will help to clear data after every test
        """
        self.user.clear()

    def test_sign_up_user(self):
        """
        Test api if it can register a new user
        """
        response = self.app.post('/api/v1/auth/register', 
                    data=json.dumps(self.user),
                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', str(response.data))

    def test_can_not_create_duplicate_user(self):
        """
        Test api can only allow one user creation
        """
        response = self.client.post('/api/v1/auth/register',
                    data=json.dumps(self.user),
                    content_type='application/json')
        response1 = self.client.post('/api/v1/auth/register',
                    data=json.dumps(self.user),
                    content_type='application/json')
        assert b'{\n "message": "username already taken!"\n}\n' in response1.data

    def test_some_details_missing(self):
        """
        Test api to ensure no details are ommited 
        """
        response = self.client.post('/api/v1/auth/register',
                    data=json.dumps({
                        "username":"",
                        "password":"",
                        "first_name":"Maestro",
                        "last_name":"Tsofa"
                    }),
                    content_type='application/json')
        assert b'{\n "message": "username and password are missing" \n}\n' in response.data


        
        
    def test_sign_in_user(self):
        """
        Test api if it can sign in existing user
        """
        response = self.app.post('/api/v1/auth/register',
                    data=json.dumps(self.user),
                    content_type='application/json')
                    
        self.assertEqual(response.status_code, 200)
        
        
    def test_sign_out_user(self):
        """
        Test api can sign out a user
        """
        response = self.app.post('/api/v1/auth/logout',
                    data=json.dumps(self.user),
                    content_type='application/json')
                    
        self.assertEqual(response.status_code, 200)
        
        
        
if __name__=='__main__':
    unittest.main()
        
        
    

