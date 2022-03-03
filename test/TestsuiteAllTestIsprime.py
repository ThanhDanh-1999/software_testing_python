import os 
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.com.thdanh.primenumber.core.isprime import *

# unitest for isprime function 
def test_isprime():
    assert isprime(1) == False
    assert isprime(2) == True
    assert isprime(10) == False
    assert isprime(11) == True
    assert isprime(25) == False

if __name__ == '__main__':
    test_isprime()
    print('all test passed')