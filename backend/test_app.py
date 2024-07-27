import unittest
from app import app  # Adjust this import based on your file structure
from io import BytesIO

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_missing_file(self):
        response = self.app.post('/process', data={'websiteUrl': 'http://example.com'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing file or URL', response.get_data(as_text=True))

    def test_missing_url(self):
        response = self.app.post('/process', data={'questionsFile': (BytesIO(b'Question?'), 'questions.txt')})
        self.assertEqual(response.status_code, 400)
        self.assertIn('File or URL not provided', response.get_data(as_text=True))

    def test_incorrect_url_format(self):
        response = self.app.post('/process', data={'questionsFile': (BytesIO(b'Question?'), 'questions.txt'), 'websiteUrl': 'not_a_url'})
        self.assertEqual(response.status_code, 500)
        self.assertIn('Failed to retrieve product data', response.get_data(as_text=True))

if __name__ == '__main__':
        unittest.main()
