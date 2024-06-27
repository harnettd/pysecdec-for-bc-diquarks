"""Compute the additional_prefactor used in a pySecDec generate file."""
from sympy import symbols, sympify


def get_additional_prefactor(
        dimensionality, 
        num_loops: int, 
        masses: list[float, float]
    ):
    """
    Return the additional_prefactor parameter for a pySecDec generate file.

    :param dimensionality: The spacetime dimension in terms of the regulator
    :type: A sympy expression

    :param num_loops: The number of loops in the integral
    :type num_loops: int

    :param masses: Two propagator masses
    :type masses: list[float, float]

    :return: The additional_prefactor parameter value
    :rtype: A sympy expression
    """
    # renormalization scale
    scale = (masses[0] + masses[1]) / 2

    dim = symbols('dim')
    additional_prefactor_per_loop =\
        sympify(f'{scale} ** (4 - dim) / (I * pi ** (dim / 2))')

    additional_prefactor = additional_prefactor_per_loop ** num_loops

    return additional_prefactor.subs(dim, dimensionality)


if __name__ == '__main__':
    print(__doc__)
