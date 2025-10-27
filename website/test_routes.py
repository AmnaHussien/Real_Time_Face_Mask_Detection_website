import unittest
from website import app

class FlaskRoutesTest(unittest.TestCase):
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Face Mask Detection', response.data)

    def test_video_feed(self):
        response = self.app.get('/video_feed')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
