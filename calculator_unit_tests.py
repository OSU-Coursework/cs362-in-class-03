# cs362 - in class activity 03
# casey nord
# spring 2021


import calculator
import unittest


class CalculatorUnitTests(unittest.TestCase):

    def test_correct_values_sum(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.sum(1, 1), 2)
        self.assertEqual(calc.sum(5, 6), 11)
        self.assertEqual(calc.sum(5, -6), -1)
    
    def test_correct_values_difference(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.difference(1, 1), 0)
        self.assertEqual(calc.difference(5, 6), -1)
        self.assertEqual(calc.difference(5, -6), 11)
    
    def test_correct_values_multiply(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.multiply(1, 1), 1)
        self.assertEqual(calc.multiply(5, 6), 30)
        self.assertEqual(calc.multiply(5, -6), -30)

    def test_correct_values_divide(self):
        calc = calculator.Calculator()
        self.assertEqual(calc.divide(1, 1), 1)
        self.assertEqual(calc.divide(30, 6), 5)
        self.assertEqual(calc.divide(30, -6), -5)

    def test_type(self):
        calc = calculator.Calculator()
        with self.assertRaises(TypeError):
            calc.sum("4", 2)
            calc.difference("4", 2)
            calc.multiply("4", 2)
            calc.divide("4", 2)


if __name__ == '__main__':
    unittest.main()
