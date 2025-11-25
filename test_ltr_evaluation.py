from unittest import TestCase
import ltr_evaluation as ltr

class Test(TestCase):
    def test_eval_ok(self):
        self.assertEqual(ltr.eval('1+2'), 3)
        self.assertAlmostEqual(ltr.eval('( 10.75 - 3.93 ) * 2. - 13.4568 / 2.075'), 0.0882, places=3)
        expr = "(3 + (2 * 10 / (40 - 20))+(3 * 4)) * 10"
        self.assertAlmostEqual(160, ltr.eval(expr))
        expr = "-3 + 2 ** -4 / -2 + -8 * -3"
        self.assertAlmostEqual(24.0024, ltr.eval(expr))
        
    def test_negative_number_error(self):
        with self.assertRaises(ValueError):
            ltr.eval('(3-23)-1 + 2')
            
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            ltr.eval('10 / 0')
        
    def test_invalid_chars(self):
        with self.assertRaises(ValueError):
            ltr.eval('2 + a')
        with self.assertRaises(ValueError):
            ltr.eval('5 & 3')
            
    def test_invalid_parentheses(self):
        with self.assertRaises(ValueError):
            ltr.eval('1 + ( 2 * 3')
        with self.assertRaises(ValueError):
            ltr.eval('1 + 2 ) * 3')
            
    def test_miplaced_operators(self):
        with self.assertRaises(ValueError):
            ltr.eval('1 + * 2')
        with self.assertRaises(ValueError):
            ltr.eval('1 + 2 * (77.88 + 3)*')