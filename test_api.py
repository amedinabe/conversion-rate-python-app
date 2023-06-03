import unittest
from api import call_get

class TestAPI(unittest.TestCase):
    """
    Class used for testing the call_get() function in api.py
    """
    def setUp(self):
        self.date = '2021-01-01'
        self.url = "https://api.frankfurter.app"+ "/" + '2021-01-01'
        
    def test_call_get(self):
        response = call_get(self.url)
        
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.json())
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
