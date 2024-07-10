"""
Generate pySecDec integral data needed for an analysis of bc-diquark masses.
"""
from pathlib import Path
from sympy import sympify

from keyhole import keyhole
from keyhole_params import *
from two_point_function import TwoPointFunction
from utils import write_domain, write_integral_vals

mcmc = str(MC ** 2)
mbmb = str(MB ** 2)

# the project directory
project_path = Path(__file__).parent.parent


def get_spec_path(name: str) -> Path:
    """
    Return the specification_path of an integral.

    :param name: The name of an integral from a generate file
    :type name: str

    :return: The specification_path parameter
    :rtype: Path

    Usage examples:
    >>> path = get_spec_path('TJI').relative_to(project_path)
    >>> str(path)
    'lib/TJI/disteval/TJI.json'
    """
    lib_path = project_path / 'lib'
    return lib_path.joinpath(name, 'disteval', f'{name}.json')


def init_integral(name: str, m1m1: str, m2m2: str) -> dict:
    """
    Initialize a dim-reg-integral dictionary.

    :param name: The integral's name from the generate file
    :type name: str

    :param m1m1: The first squared propagator mass
    :type: str

    :param m2m2: The second squared propagator mass
    :type: str

    :return: A dim-reg-integral dictionary
    :rtype: dict
    """
    return {
        'tarcer_basis_integral':
            TwoPointFunction(
                get_spec_path(name),
                {'m1m1': m1m1, 'm2m2': m2m2},
                verbose=False
            ),
        'vals': []
    }


def main():
    # Initialize all dim-reg integrals.
    integrals = {
        'tbi_1_mc_1_mb': init_integral('TBI_1_m1_1_m2', mcmc, mbmb),
        'tji_1_mc_1_mb': init_integral('TJI_1_m1_1_m2_1_0', mcmc, mbmb),
        'tji_2_mc_1_mb': init_integral('TJI_2_m1_1_m2_1_0', mcmc, mbmb),
        'tji_1_mc_2_mb': init_integral('TJI_2_m1_1_m2_1_0', mbmb, mcmc)
    }

    # Define the keyhole domain.
    domain = keyhole(
        centre=CENTRE, 
        radius=RADIUS, 
        max_re_qq=MAX_RE_QQ,
        num_pts_arc=NUM_PTS_ARC,
        num_pts_line=NUM_PTS_LINE,
        delta=DELTA
    )

    # Evaluate each integral at each point of the domain.
    for qq in domain:
        for integral_props in integrals.values():
            val = integral_props['tarcer_basis_integral']\
                .eval(sympify(qq), format="mathematica")
            integral_props['vals'].append(val)

    # Write domain to file.
    data_path = project_path / 'data'
    write_domain(domain, data_path / 'domain.m')

    # Write integral values to files.
    for name in integrals:
        write_integral_vals(
            integrals[name]['vals'],
            data_path / f'{name}-vals.m'
        )


if __name__ == '__main__':
    main()
