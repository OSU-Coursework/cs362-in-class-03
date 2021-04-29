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
    
    def test_type(self):
        calc = calculator.Calculator()
        with self.assertRaises(TypeError):
            calc.sum("4", 2)


if __name__ == '__main__':
    unittest.main()
