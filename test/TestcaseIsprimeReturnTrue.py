import os 
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.com.thdanh.primenumber.core.isprime import *

EXPECTED = True
ACTUAL = isprime(2)

# test_simple_unittest.py

class TestPrime(unittest.TestCase):

    def testprime(self):
        self.assertEqual(EXPECTED, ACTUAL)

if __name__ == '__main__':
    unittest.main(verbosity=2)