"""Utilities to help with testing."""

def complex_round(z, decimal_places=3):
    """Round a complex number."""
    return round(z.real, decimal_places) + round(z.imag, decimal_places) * 1j

if __name__ == '__main__':
    print(__doc__)
