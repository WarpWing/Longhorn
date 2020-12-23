import unittest
import requests

app = 'http://0.0.0.0:5000'

r = requests.get(app)

class MyTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(r.status_code, 200) 

    def test_apiv1(self):
        self.assertEqual(r.status_code, 200) 

    def test_kfc(self):
        self.assertEqual(r.status_code, 200)
        #self.assertEqual(r.headers['content-type'], 'application/json')

if __name__ == "__main__":
    unittest.main()