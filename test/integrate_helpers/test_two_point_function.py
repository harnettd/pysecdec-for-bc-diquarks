"""Test TwoPointFunction class."""
import unittest

from pathlib import Path
from sympy import sympify

from pysecdec_integrals.integrate_helpers.two_point_function import\
    TwoPointFunction
from pysecdec_integrals.integrate_helpers.utils import get_specification_path

from test.utils import complex_round
from test.integrate_helpers.PySecDecJSONResult import PySecDecJSONResult
from test.integrate_helpers.analytic_two_point_function import tbi_1_0_1_0

class TestTwoPointFunction(unittest.TestCase):
    def test_tbi_1_0_1_0(self):
        integral_name = 'TBI_1_m1_1_m2'
        specification_path = get_specification_path(integral_name)
        masses = {'m1m1': '0', 'm2m2': '0'}
        integral = TwoPointFunction(specification_path, masses)
        
        qq = 5.0 + 1e-4 * 1j
        result = integral.eval(sympify(qq), format='json')
        json_result = PySecDecJSONResult(result)
        json_result.round(n_digits=3).trunc_at_order(order=2)
        calc = json_result.expansion

        actual = tbi_1_0_1_0(qq)

        self.assertDictEqual(calc, actual)

    def test_tji_1_0_1_0_1_0(self):
        pass

    def test_tji_2_0_1_0_1_0(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
