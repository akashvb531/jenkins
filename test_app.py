def hello():
    return "Hello, Jenkins!"

if __name__ == "__main__":
    print(hello())


-> Add a unit test (test_app.py):

import unittest
from app import hello

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, Jenkins!")