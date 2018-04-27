"""This module tests the auth endpoint"""

import json
import unittest
from event_api.api import APP


class TestAuthEndpoint(unittest.TestCase):
    """Class that handles Auth Endpoint test"""

    def setUp(self):
        """code that is executed before each test"""
        APP.testing = True
        self.app = APP.test_client()
        self.data = {
            "username": "user1",
            "password": "password"
        }

    def test_register(self):
        """Test for successful registration"""
        response = self.app.post('/api/auth/register',
                                 data=json.dumps(self.data),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["username"], "user1")
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
