"""Some analytic results for two-point functions."""
import numpy as np

def tbi_1_0_1_0(qq: complex) -> dict:
    return {
        -1: -1j,
        0: 1j * (2 - np.euler_gamma - np.log(-qq / (4 * np.pi)))
    }

if __name__ == '__main__':
    print(tbi_1_0_1_0(qq=5.0 + 1e-4 * 1j))
