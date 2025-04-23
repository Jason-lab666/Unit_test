import unittest
from prime import is_prime

class testPrime(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))

    def test_non_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(40))

if __name__ == "__main__":
    unittest.main()
    