# app/tests/test_user.py

import os
import unittest
import json
from app import create_app

class CreateUserTestCase(unittest.TestCase):
    """
    The api test case class
    """
    def setUp(self):
        """
        This method will be called before every time a test runs, 
        and will create data for use by the tests
        """
        self.app = create_app(config_name="testing")
        create_app.testing = True
        self.client = self.app.test_client

        self.test_user = {
            "username":"testuser",
            "name":"Test User",
            "email":"test_user@maintenance_tracker.com",
            "password":"testuser123",
            "confirm_password": "testuser123"
        }
        self.reset_password = {
            "current_password": "Testuser123",
            "new_password" : "userTest321",
            "confirm_new_password" : "userTest321"
        }
        self.sign_in_user = {
            "username": "sign_in_user",
            "password": "sign_in123"
        }

    def tearDown(self):
        """
        Clears data after every test run
        """
        self.test_user.clear()
        self.reset_password.clear()
        self.sign_in_user.clear()


    def test_sign_up_user(self):
        """
        Test api if it can register a new user
        """
        response = self.client().post('/api/v1/auth/register', 
                    data=json.dumps(self.test_user),
                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', str(response.data))

    def test_can_not_create_duplicate_user(self):
        """
        Test api can only allow one username creation
        """
        response = self.client().post('/api/v1/auth/register',
                    data=json.dumps(self.test_user),
                    content_type='application/json')
        response1 = self.client().post('/api/v1/auth/register',
                    data=json.dumps(self.test_user),
                    content_type='application/json')
        self.assertIn("username already exists", str(response.data))

    def test_blank_username(self):
        """
        Test api for blank usernames 
        """
        response = self.client().post('/api/v1/auth/register',
                    data=json.dumps({
                        "username":"",
                        "password":"testuser123",
                        "first_name":"test",
                        "last_name":"user"
                    }),
                    content_type='application/json')
        self.assertIn("username missing", str(response.data))

    def test_blank_password(self):
        """
        Test api for blank password 
        """
        response = self.client().post('/api/v1/auth/register',
                    data=json.dumps({
                        "username":"testuser",
                        "password":"",
                        "first_name":"test",
                        "last_name":"user"
                    }),
                    content_type='application/json')
        self.assertIn("username missing", str(response.data))
        
    def test_can_sign_in_user(self):
        """
        Test api if it can sign in existing user
        """
        self.client().post('/api/v1/auth/register',
                    data=json.dumps(self.test_user),
                    headers={'content_type=':'application/json'})
        response = self.client().post('/api/v1/auth/signin',
                    data=json.dumps(self.test_user),
                    content_type='application/json')            
        self.assertEqual(response.status_code, 200)
        
    def test_sign_out_user(self):
        """
        Test api can sign out a user
        """
        response = self.client().post('/api/v1/auth/logout',
                    data=json.dumps(self.sign_in_user),
                    headers={'content_type=':'application/json',
                            'x-access-token':self.token})
        self.assertIn("You're now logged out", str(response.data))            
        self.assertEqual(response.status_code, 200)
        
        
        
if __name__=='__main__':
    unittest.main()