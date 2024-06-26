"""Utilities for writing data to file."""
from numpy import ndarray
from pathlib import Path


def complex_to_str(c: complex) -> str:
    """
    Return a complex number as a string.

    Usage examples:
    >>> complex_to_str(2.0 - 3.2j)
    '(2.0) + (-3.2)*I'
    >>> complex_to_str(3)
    '(3) + (0)*I'
    >>> complex_to_str(-4.5j)
    '(-0.0) + (-4.5)*I'
    """
    return f'({c.real}) + ({c.imag})*I'


def write_domain(domain: ndarray, path: Path) -> None:
    """
    Write an array of domain elements to file.

    The output file is intended to be a .m file that
    can be read into Mathematica.

    :param domain: The domain
    :type domain: ndarray

    :param path: The path of the output file
    :type path: Path
    """
    complex_strings = [complex_to_str(pt) for pt in domain]
    with open(path, 'w') as file:
        file.write('{')
        file.writelines(',\n'.join(complex_strings))
        file.write('}')


def write_integral_vals(integral_values: list, path: Path) -> None:
    """
    Write a list of integral values to file.

    The output file is intended to be a .m file that can
    be read directly into Mathematica. 
    """
    with open(path, 'w') as file:
        file.write('{')
        file.writelines(',\n'.join(integral_values))
        file.write('}')


if __name__ == '__main__':
    print(__doc__)
  