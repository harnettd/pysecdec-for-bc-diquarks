"""Utilities for writing pySecDec-integral data to file."""
from numpy import ndarray
from pathlib import Path

from pysecdec_integrals import PROJECT_PATH


def get_specification_path(name: str) -> Path:
    """
    Return the specification_path of an integral.

    :param name: The name of an integral from a generate file
    :type name: str

    :return: The specification_path parameter
    :rtype: Path

    Usage examples:
    >>> path = get_specification_path('TJI').relative_to(PROJECT_PATH)
    >>> str(path)
    'TJI/disteval/TJI.json'
    """
    return PROJECT_PATH.joinpath(name, 'disteval', f'{name}.json')


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
    Write an array of calc elements to file.

    The output file is intended to be a .m file that
    can be read into Mathematica.

    :param domain: The calc
    :type domain: ndarray

    :param path: The path of the output file
    :type path: Path
    """
    complex_strings = [complex_to_str(pt) for pt in domain]
    with open(path, 'w', encoding='utf-8') as file:
        file.write('{')
        file.write(',\n'.join(complex_strings))
        file.write('}')


def write_integral_vals(integral_vals: list, path: Path) -> None:
    """
    Write a list of integral values to file.

    The output file is intended to be a .m file that can
    be read directly into Mathematica. 

    :param integral_vals: pySecDec-computed integral values
    :type integral_vals: list

    :param path: The path of the output file
    :type path: Path
    """
    with open(path, 'w') as file:
        file.write('{')
        file.write(',\n'.join(integral_vals))
        file.write('}')


if __name__ == '__main__':
    print(__doc__)
  