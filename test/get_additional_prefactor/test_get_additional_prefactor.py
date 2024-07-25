"""Test get_additional_prefactor() function."""
import unittest

from sympy import symbols, simplify, sympify

from pysecdec_integrals.get_additional_prefactor.get_additional_prefactor\
    import get_additional_prefactor

eps = symbols('eps')

class TestGetAdditionalPrefactor(unittest.TestCase):
    def test_one_loop(self):
        """Test one-loop prefactor."""
        calc = get_additional_prefactor(
            dimensionality=4 + 2 * eps,
            num_loops=1,
            renorm_scale=2.0
        )
        actual = sympify('I / (4.0 ** eps)')
        self.assertEqual(simplify(calc - actual), 0)

    def test_two_loops(self):
        """Test two-loop prefactor."""
        calc = get_additional_prefactor(
            dimensionality=4 - 2 * eps,
            num_loops=2,
            renorm_scale=3.0
        )
        actual = sympify('-81.0 ** eps')
        self.assertEqual(simplify(calc - actual), 0)

    def test_three_loops(self):
        """Test three-loop prefactor."""
        calc = get_additional_prefactor(
            dimensionality=4 + 2 * eps,
            num_loops=3,
            renorm_scale=4.0
        )
        actual = sympify('-I / (4.0 ** (6 * eps))')
        self.assertEqual(simplify(calc - actual), 0)

    def test_four_loops(self):
        """Test four-loop prefactor."""
        calc = get_additional_prefactor(
            dimensionality=4 - 2 * eps,
            num_loops=4,
            renorm_scale=5.0
        )
        actual = sympify('5.0 ** (8 * eps)')
        self.assertEqual(simplify(calc - actual), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
