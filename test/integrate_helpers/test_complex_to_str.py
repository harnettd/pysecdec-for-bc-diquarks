import unittest

from pysecdec_integrals.integrate_helpers.utils import complex_to_str

class TestComplexToStr(unittest.TestCase):
    def test_generic(self):
        """Test generic complex number."""
        self.assertEqual(complex_to_str(2 + 3j), '(2.0) + (3.0)*I')
        self.assertEqual(complex_to_str(-1 + 1j), '(-1.0) + (1.0)*I')
        self.assertEqual(complex_to_str(-2.56 - 3.14j), '(-2.56) + (-3.14)*I')

    def test_zero_im_part(self):
        """Test zero imaginary part."""
        self.assertEqual(complex_to_str(4), '(4) + (0)*I')
        self.assertEqual(complex_to_str(-1.1), '(-1.1) + (0.0)*I')

    def test_zero_re_part(self):
        """Test zero real part."""
        self.assertEqual(complex_to_str(9j), '(0.0) + (9.0)*I')
        self.assertEqual(complex_to_str(-4.5j), '(-0.0) + (-4.5)*I')

if __name__ == '__main__':
    unittest.main(verbosity=2)
