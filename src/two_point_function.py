"""
An implmentation of dimensionally-regularized two-point functions.

This class is a very thin layer on top of the DistevalLibrary class
from pySecDec. A two-point function has precisely one external momentum 
and any number of propagator masses. The propagator masses are supplied
once at instantiation. Then, the external (squared) momentum is the only 
parameter that needs to be passed for an integral evaluation.

Attributes:
    disteval_lib (DistevalLibrary): the underlying pySecDec DistevalLibrary
    squared_masses (dict): squared propagator masses 

Methods:
    eval: evaluate the integral at a given squared external momentum
"""
from pathlib import Path
from typing import Union

from pySecDec.integral_interface import DistevalLibrary


class TwoPointFunction:

    def __init__(
            self, 
            specification_path: Union[str, Path], 
            squared_masses: dict[str],
            workers=None,
            verbose=False
        ) -> None:
        """
        Define a dimensionally-regularized two-point function.

        Descriptions for the parameters specification_path, workers, 
        and verbose can be found at:
        https://secdec.readthedocs.io/en/stable/full_reference.html#integral-interface

        :param squared_masses: squared propagator masses
        :type squared_masses: dict[str]
        """
        self.disteval_lib =\
            DistevalLibrary(specification_path, workers, verbose)
        self.squared_masses = squared_masses
        
    def eval(self, qq, **kwargs) -> str:
        """
        Evaluate the two-point function.

        :param qq: Squared external momentum
        """
        parameters = {**self.squared_masses}
        parameters['qq'] = qq
        result = self.disteval_lib(parameters=parameters, **kwargs)
        return result


if __name__ == '__main__':
    print(__doc__)
