from unittest import TestCase
import unittest

class TestApp(TestCase):
    def test_succeeding(self):
        self.assertTrue(True)

    @unittest.skip
    def test_failing(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main() >> open('logs/test.log', 'w')
