import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Test with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)
        
        # Test with decimals
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(1.1, 2.2), 3.3)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test with decimals
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertEqual(self.calc.subtract(10.7, 3.2), 7.5)
        
        # Test result that should be zero
        self.assertEqual(self.calc.subtract(5, 5), 0)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-5, -4), 20)
        self.assertEqual(self.calc.multiply(5, -3), -15)
        
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Test with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        
        # Test with decimals
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(3.5, 2), 7.0)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test positive numbers
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(20, 4), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test division resulting in decimal
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(7, 4), 1.75)
        
        # Test division with decimals
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        
        # Test division by one
        self.assertEqual(self.calc.divide(10, 1), 10.0)
        
        # Test zero divided by a number
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_by_zero(self):
        """Test the division method with division by zero."""
        # Test division by zero returns None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-10, 0))
        self.assertIsNone(self.calc.divide(0, 0))


if __name__ == "__main__":
    unittest.main()
