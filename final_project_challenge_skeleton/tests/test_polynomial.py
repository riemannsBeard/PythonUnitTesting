"""
    This is just an example to get you started.
    Here are some ideas on things you should test for:
    1- Test for None values.
    2- Test if the multiply method in the Polynomial class still works even if:
        - the power is zero or lower.
        - the coefficient is zero or lower.
        Note: we need to test the above because we might do some math that cases errors.
    3- Test if the print_poly method prints terms in ascending order.
"""

import sys
import unittest
from term import Term
from polynomial import Polynomial
from io import StringIO


class TestPolynomialMultiplier(unittest.TestCase):

    def setUp(self):
        self._first_polynomial = Polynomial([Term(2, 2), Term(2, 3)])
        self._second_polynomial = Polynomial([Term(2, 4), Term(2, 2)])
        self._result = {6: 4,
                        4: 4,
                        7: 4,
                        5: 4}

        self._none_polynomial = Polynomial([None, Term(2, 3)])
        self._zero_power_polynomial = Polynomial([Term(2, 0)])
        self._zero_coeff_polynomial = Polynomial([Term(0, 5)])

    def test_multiply_one(self):
        self._first_polynomial.multiply(self._second_polynomial)
        for k, v in self._first_polynomial.get_result().items():
            self.assertEqual(self._first_polynomial.get_result().get(k), self._result.get(k))

    def test_multiply_two(self):
        with self.assertRaises(TypeError):
            self._first_polynomial.multiply(self._none_polynomial)

    def test_multiply_three(self):
        self._first_polynomial.multiply(self._zero_coeff_polynomial)
        for k, v in self._first_polynomial.get_result().items():
            self.assertEqual(self._first_polynomial.get_result().get(k), 0)

    def test_multiply_four(self):
        self._first_polynomial.multiply(self._zero_power_polynomial)
        for k, v in self._first_polynomial.get_result().items():
            self.assertEqual(self._first_polynomial.get_result().get(k), self._first_polynomial.get_result().get(k) *
                             2.0)

    def tearDown(self):
        self._term = None


class TestPolynomialPrint(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_print(self):
        self._polynomial = Polynomial([Term(2, 2), Term(2, 5), Term(7, 3), Term(1, 4)])
        self._polynomial.print_poly()
        self.assertEqual(sys.stdout.getvalue().strip(), '2 x^2, 7 x^3, 1 x^4, 2 x^5')

    def tearDown(self):
        self.printer = None


if __name__ == '__main__':
    unittest.main()