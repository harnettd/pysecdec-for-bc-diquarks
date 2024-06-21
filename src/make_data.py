"""
Generate pySecDec data.
"""
import numpy as np

from pathlib import Path
from sympy import sympify

from tarcer_basis_integral import TarcerBasisIntegral

MC = 1.2  # charm quark mass
MB = 4.5  # bottom quark mass
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


def keyhole(
        centre: float, 
        radius: float, 
        max_re_qq: float,
        num_pts_half_circle: int, 
        num_pts_line: int,
        delta: float = 1e-6) -> np.array:
    """
    Return a keyhole
    """
    assert isinstance(centre, float)
    assert radius > 0 
    assert max_re_qq > centre + radius
    assert isinstance(num_pts_line, int)
    assert isinstance(num_pts_half_circle, int)
    assert delta > 0 
    assert delta < radius

    min_re_qq = centre + np.sqrt(radius ** 2 + delta ** 2)
    max_theta = np.arctan(delta / min_re_qq)

    thetas = np.linspace(np.pi, max_theta, num_pts_half_circle,
                         dtype=np.complex64)
    
    arc = centre + radius * np.exp(thetas[1:] * 1j)
    np.insert(arc, 0, centre - radius)

    qq_line = np.linspace(min_re_qq, max_re_qq, num_pts_line, 
                          dtype=np.complex64) + delta * 1j

    return np.concatenate((arc[:-1], qq_line))


def complex_to_str(c):
    return f'({c.real}) + ({c.imag})*I'


def write_domain(domain, path):
    tmp = [complex_to_str(p) for p in domain]
    with open(path, 'w') as file:
        file.write('{')
        file.writelines(',\n'.join(tmp))
        file.write('}')


def write_integral_vals(integral_values: list, path):
    with open(path, 'w') as file:
        file.write('{')
        file.writelines(',\n'.join(integral_values))
        file.write('}')    


def main():
    # Define all dim-reg integrals.
    integrals = {
        'tbi_1_mc_1_mb': {
            'specification_path': get_spec_path('TBI_1_m1_1_m2'),
            'squared_masses': {'m1m1': mcmc, 'm2m2': mbmb},
            'tarcer_basis_integral': None,
            'corr_vals': []
        },
        'tji_1_mc_1_mb': {
            'specification_path': get_spec_path('TJI_1_m1_1_m2_1_0'),
            'squared_masses': {'m1m1': mcmc, 'm2m2': mbmb},
            'tarcer_basis_integral': None,
            'corr_vals': []
        },
        'tji_2_mc_1_mb': {
            'specification_path': get_spec_path('TJI_2_m1_1_m2_1_0'),
            'squared_masses': {'m1m1': mcmc, 'm2m2': mbmb},
            'tarcer_basis_integral': None,
            'corr_vals': []
        },
        'tji_1_mc_2_mb': {
            'specification_path': get_spec_path('TJI_2_m1_1_m2_1_0'),
            'squared_masses': {'m1m1': mbmb, 'm2m2': mcmc},
            'tarcer_basis_integral': None,
            'corr_vals': []
        }
    }

    for props in integrals.values():
        props['tarcer_basis_integral'] =\
            TarcerBasisIntegral(
                specification_path=props['specification_path'],
                squared_masses=props['squared_masses'],
                verbose=False
            )

    # Define the domain.
    domain = keyhole((MC + MB) ** 2, 1.5, 50, 5, 5, 1e-3)

    # Evaluate each integral at each point of the domain.
    for qq in domain:
        # print(f'qq = {qq}')
        for props in integrals.values():
            int_val = props['tarcer_basis_integral'].eval(sympify(qq), format="mathematica")
            props['corr_vals'].append(int_val)
            # print(f'int_val = {int_val}')
        # print()

    # Write domain to file.
    data_path = project_path.joinpath('data')
    write_domain(domain, data_path.joinpath('domain.m'))

    # Write integral values to files.
    for name in integrals:
        write_integral_vals(
            integrals[name]['corr_vals'],
            data_path.joinpath(f'{name}-vals.m')
        )


if __name__ == '__main__':
    main()
