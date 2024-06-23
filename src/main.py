"""
Generate pySecDec integral data needed for an analysis of bc-diquark masses.
"""
from pathlib import Path
from sympy import sympify

from keyhole import keyhole
from tarcer_basis_integral import TarcerBasisIntegral
from utils import write_domain, write_integral_vals

MC = 1.27 
MB = 4.18
mcmc = str(MC ** 2)
mbmb = str(MB ** 2)

# the project directory
project_path = Path(__file__).parent.parent


def get_spec_path(name: str) -> Path:
    """
    Return the specification_path of an integral.

    :param integral_name: The name of an integral from a generate file
    :type integral_name: str

    :return: The specification_path parameter
    :rtype: Path
    """
    # It is assumed that the generate files are contained in lib/, a
    # directory in the project directory.
    lib_path = project_path.joinpath('lib')
    return lib_path\
        .joinpath(name)\
        .joinpath('disteval')\
        .joinpath(f'{name}.json')


def init_integral(name: str, m1m1: str, m2m2: str) -> dict:
    """
    Initialize a dim-reg-integral dictionary.

    :param name: The integral's name from the generate file
    :type name: str

    :param m1m1: The first squared propagator mass
    :type: str

    :param: The second squared propagator mass
    :type: str

    :return: A dim-reg-integral dictionary
    :rtype: dict
    """
    return {
        'tarcer_basis_integral':
            TarcerBasisIntegral(
                get_spec_path(name),
                {'m1m1': m1m1, 'm2m2': m2m2},
                verbose=False
            ),
        'vals': []
    }


def main():
    # Initialize all dim-reg integrals.
    integrals = {}
    integrals['tbi_1_mc_1_mb'] =\
        init_integral('TBI_1_m1_1_m2', mcmc, mbmb)
    integrals['tji_1_mc_1_mb'] =\
        init_integral('TJI_1_m1_1_m2_1_0', mcmc, mbmb)
    integrals['tji_2_mc_1_mb'] =\
        init_integral('TJI_2_m1_1_m2_1_0', mcmc, mbmb)
    integrals['tji_1_mc_2_mb'] =\
        init_integral('TJI_2_m1_1_m2_1_0', mbmb, mcmc)

    # Define the keyhole domain.
    domain = keyhole(
        centre=(MC + MB) ** 2, 
        radius=1.5, 
        max_re_qq=75, 
        num_pts_arc=5, 
        num_pts_line=10, 
        delta=1e-3
    )

    # Evaluate each integral at each point of the domain.
    for qq in domain:
        for integral_props in integrals.values():
            val = integral_props['tarcer_basis_integral']\
                .eval(sympify(qq), format="mathematica")
            integral_props['vals'].append(val)

    # Write domain to file.
    data_path = project_path.joinpath('data')
    write_domain(domain, data_path.joinpath('domain.m'))

    # Write integral values to files.
    for name in integrals:
        write_integral_vals(
            integrals[name]['vals'],
            data_path.joinpath(f'{name}-vals.m')
        )


if __name__ == '__main__':
    main()
