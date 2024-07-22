"""Compute the additional_prefactor used in a pySecDec generate file."""
from sympy import symbols, sympify


def get_additional_prefactor(
        dimensionality, 
        num_loops: int, 
        renorm_scale: float
    ):
    """
    Return the additional_prefactor parameter for a pySecDec generate file.

    :param dimensionality: The spacetime dimension in terms of the regulator
    :type: A sympy expression

    :param num_loops: The number of loops in the integral
    :type num_loops: int

    :param renorm_scale: Renormalization scale
    :type renorm_scale: float

    :return: The additional_prefactor parameter value
    :rtype: A sympy expression

    Usage examples:
    >>> from sympy import simplify
    >>> eps = symbols('eps')
    >>> calc = get_additional_prefactor(4 + 2 * eps, 1, 2.0)
    >>> actual = sympify("I / (4.0 ** eps)")
    >>> simplify(calc - actual)
    0
    """
    dim = symbols('dim')  # spacetime dimension

    additional_prefactor_per_loop =\
        sympify(f'I * {renorm_scale} ** (4 - dim)')

    additional_prefactor = additional_prefactor_per_loop ** num_loops

    return additional_prefactor.subs(dim, dimensionality)


if __name__ == '__main__':
    print(__doc__)
