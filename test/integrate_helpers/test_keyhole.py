import unittest

import numpy as np

from pysecdec_integrals.integrate_helpers.keyhole import keyhole
from test.utils import complex_round

CENTRE = 5.0
RADIUS = 2.0
MAX_RE_QQ = 11.0
NUM_PTS_ARC = 5
NUM_PTS_LINE = 5
DELTA = 1e-9


class TestKeyhole(unittest.TestCase):
    def setUp(self):
        self.calc = keyhole(
            centre=CENTRE,
            radius=RADIUS,
            max_re_qq=MAX_RE_QQ,
            num_pts_arc=NUM_PTS_ARC,
            num_pts_line=NUM_PTS_LINE,
            delta=DELTA
        )

        self.actual = np.array([
            3.0,
            5.0 + 2.0 / np.sqrt(2.0) * (-1 + 1j),
            5.0 + 2.0j,
            5.0 + 2.0 / np.sqrt(2.0) * (1 + 1j),
            7.0, 8.0, 9.0, 10.0, 11.0
        ], dtype=np.complex64)

    def test_type(self):
        """Test the keyhole type."""
        self.assertIsInstance(self.calc, np.ndarray)

    def test_len(self):
        """Test the keyhole length."""
        self.assertEqual(len(self.calc), len(self.actual))

    def test_element_types(self):
        """Test the types of the keyhole elements."""
        for z in self.calc:
            with self.subTest(z=z):
                self.assertIsInstance(z, np.complex64)

    def test_signs_imaginary_parts(self):
        """Test the signs of the imaginary parts of the keyhole elements."""
        for z in self.calc:
            with self.subTest(z=z):
                self.assertTrue(z.imag >= 0)

    def test_element_values(self):
        """Test the values of the keyhole elements."""
        for idx in range(len(self.calc)):
            with self.subTest(idx=idx):
                self.assertEqual(
                    complex_round(self.calc[idx], 6),
                    complex_round(self.actual[idx], 6)
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
