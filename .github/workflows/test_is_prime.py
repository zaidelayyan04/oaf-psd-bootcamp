import unittest
from is_prime import is_prime
class TestIsPrime(unittest.TestCase):
  
  # functional
  def test_prime_numbers(self):
    self.assertTrue(is_prime(2))
    self.assertTrue(is_prime(3))
    self.assertTrue(is_prime(5))
    self.assertTrue(is_prime(13))

  def test_non_prime(self):
    self.asssertFalsse(is_prime(1))
    self.assertFalse(is_prime(4))
    self.assertFalse(is_prime(9))
    self.assertFalse(is_prime(10))
    
  


    
