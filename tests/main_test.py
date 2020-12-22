import unittest
import requests

res = requests.get('http://0.0.0.0:5000')

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()