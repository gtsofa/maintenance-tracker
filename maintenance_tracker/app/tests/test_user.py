# app/tests/v1/test_user.py

import sys
import unittest
import json
from app.views import app

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
        #create_app.testing = True
        #self.user = User()
        #self.request = Request()
        
    def test_sign_up_user(self):
        """
        Test api if it can register a new user
        """
        new_user_maestro = {
            "username":"maestro",
            "name":"Maestro Tsofa",
            "email":"maestro@maintenance_tracker.com",
            "password":"amka123"
        }
        
        response = self.app.post('/api/v1/auth/register', 
                    data=json.dumps(new_user_maestro),
                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', str(response.data))
        
        
    def test_sign_in_user(self):
        """
        Test api if it can sign in a user who have an account with app
        """
        user_logout_maestro = {
            "email":"maestro@maintenance_tracker.com",
            "password":"amka123"
        }
        response = self.app.post('/api/v1/auth/register',
                    data=json.dumps(user_logout_maestro),
                    content_type='application/json')
                    
        self.assertEqual(response.status_code, 200)
        
        
    def test_sign_out_user(self):
        """
        Test api can sign out a user
        """
        user_logout_mloi = {
            "username":"Maestro",
            "password":"amka123"
        }
        response = self.app.post('/api/v1/auth/logout',
                    data=json.dumps(user_logout_mloi),
                    content_type='application/json')
                    
        self.assertEqual(response.status_code, 200)
        
    def tearDown(self):
        """
        This method will be called after the tests run. 
        It will help to clear data after every test
        """
        self.user.clear()
        self.request.clear()
        
        
        
if __name__=='__main__':
    unittest.main()
        
        
    

