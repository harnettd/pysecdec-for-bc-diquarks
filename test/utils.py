def complex_round(z, n=3):
    """Round a complex number."""
    return round(z.real, n) + round(z.imag, n) * 1j