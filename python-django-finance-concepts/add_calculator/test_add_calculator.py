# UNITTEST: Test_Driven Development Principle States that unittest is to be built before building the functionality for that given task.
# Build a simple addition calculator

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator

    def test_add(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
        self.assertEqual(self.calc.add(0,0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(1,1), 0)
        self.assertEqual(self.calc.subtract(0,0), 0)
        self.assertEqual(self.calc.subtract(2,5), -3)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
