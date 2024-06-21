"""Tarcer basis integral class"""
from pySecDec.integral_interface import DistevalLibrary
from sympy import sympify


class TarcerBasisIntegral:

    def __init__(
            self, 
            specification_path: str, 
            squared_masses: dict[str],
            workers=None,
            verbose=False
        ) -> None:
        """
        Define a Tarcer basis integral
        """
        self.disteval_lib =\
            DistevalLibrary(specification_path, workers, verbose)
        self.squared_masses = squared_masses
        
    def eval(self, qq, **kwargs) -> str:
        """
        Evaluate an integral.
        """
        parameters = {**self.squared_masses}
        parameters['qq'] = qq
        result = self.disteval_lib(parameters=parameters, **kwargs)
        return result


if __name__ == '__main__':
    # print(__doc__)

    from pathlib import Path
    
    project_path = Path(__file__).parent.parent
    lib_path = project_path.joinpath('lib')
    json_path = lib_path\
        .joinpath('TBI_1_m1_1_m2')\
        .joinpath('disteval')\
        .joinpath('TBI_1_m1_1_m2.json')
    
    tbi = TarcerBasisIntegral(json_path, {'m1m1': '1.2', 'm2m2': '4.2'})
    result = tbi.eval(qq=sympify(31.0 - 1e-3j), format='mathematica', epsrel=1e-6, epsabs=1e-9)
    print(result)
