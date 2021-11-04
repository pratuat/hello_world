from unittest import TestCase
import unittest

class TestApp(TestCase):
    def test_app(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main() >> open('logs/test.log', 'w')
