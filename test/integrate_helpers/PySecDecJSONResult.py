"""A class for pySecDec JSON results."""
from test.utils import complex_round

class PySecDecJSONResult:
    def __init__(self, result):
        integrals = result['integrals']
        self.integral_name = list(integrals.keys())[0]        
        exp_val_err = integrals[self.integral_name]
        exponents = [key[0] for key in exp_val_err.keys()]
        values = [val for (val, err) in exp_val_err.values()]
        self.expansion = {e: v for (e, v) in zip(exponents, values)}

    @staticmethod
    def apply_to_vals(d: dict, f):
        return {key: f(val) for (key, val) in d.items()}

    def round(self, n_digits=3):
        self.expansion = PySecDecJSONResult.apply_to_vals(
            self.expansion, 
            lambda z: complex_round(z, n_digits)
        )
        return self

    def trunc_at_order(self, order: int):
        self.expansion = {
            key: val for (key, val) in self.expansion.items() if key <= order
        }
        return self

    def __str__(self):
        integral_name = str(f'Integral name: {self.integral_name}')
        exponents = f'Exponents: {list(self.expansion.keys())}'
        values = f'Values: {list(self.expansion.values())}'
        return '\n'.join([integral_name, exponents, values])

if __name__ == '__main__':
    print(__doc__)

    from sympy import sympify

    from pysecdec_integrals.integrate_helpers.two_point_function import TwoPointFunction
    from pysecdec_integrals.integrate_helpers.utils import get_specification_path

    integral_name = 'TBI_1_m1_1_m2'
    integral = TwoPointFunction(
        get_specification_path(integral_name),
        {'m1m1': '0', 'm2m2': '0'}
    )

    qq = sympify('5.0 + 0.001 * I')
    result = integral.eval(qq, format='json')
    print(result)
    print()
    
    json_result = PySecDecJSONResult(result)
    print(json_result)
    print()

    json_result.round(3).trunc_at_order(0)
    print(json_result)
    print()

    # json_result.trunc_at_order(0)
    # print(json_result)
    # print()
