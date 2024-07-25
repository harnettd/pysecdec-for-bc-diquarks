import unittest

from pathlib import Path
from sympy import sympify

# from pysecdec_integrals import PROJECT_PATH
from pysecdec_integrals.integrate_helpers.two_point_function import\
    TwoPointFunction
from pysecdec_integrals.integrate_helpers.utils import get_specification_path

from test.utils import complex_round

class TestTwoPointFunction(unittest.TestCase):
    @staticmethod
    def parse_result(result, integral_name):
        expansion = result['integrals'][f'{integral_name}_integral']
        exponents = [exponent[0] for exponent in expansion.keys()]
        values = [val for (val, err) in expansion.values()]
        return {e: v for (e, v) in zip(exponents, values)}

    def test_tbi_1_0_1_0(self):
        integral_name = 'TBI_1_m1_1_m2'
        specification_path = get_specification_path(integral_name)
        masses = {'m1m1': '0', 'm2m2': '0'}
        integral = TwoPointFunction(specification_path, masses)
        
        qq = '5.0 + 0.000_1 * I'
        result = integral.eval(sympify(qq), format='json')
        parsed_result = TestTwoPointFunction.parse_result(result, integral_name)
        parsed_result =\
            {e: complex_round(v, 3) for (e, v) in parsed_result.items()}
        
        actual = {
            -1: -0.0 - 1.0j,
            0: -3.142 + 1.818j,
            1: 5.712 + 2.104j,
            2: -3.725 - 5.968j
        }

        self.assertDictEqual(parsed_result, actual)

    def test_tji_1_0_1_0_1_0(self):
        pass

    def test_tji_2_0_1_0_1_0(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
