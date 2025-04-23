import unittest
from my_module import add

class Test_add(unittest.TestCase):

    def add_positive(self):
        self.assertEqual(add(2,3),5)

    def add_negative(self):
        self.assertEqual(add(-2,-4),-6)

    def add_zero(self):
        self.assertEqual(add(0,0),0)

if __name__ == '__main__':
    unittest.main()