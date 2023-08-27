"""
unit test tutorial
"""
import unittest
import calc

class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(8,9), 17)
        self.assertEqual(calc.add(0,-1), -1)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(6,7), -1)
        self.assertEqual(calc.subtract(0,-1), +1)
    
    def test_divide(self):
        self.assertEqual(calc.divide(9,3), 3)
        self.assertRaises(ZeroDivisionError,calc.divide,4, 0) # test raised exception.
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(1,2),2)
        self.assertEqual(calc.multiply(9,0),0)
    


if __name__ == '__main__':
    unittest.main()
