"""Parameters needed to define a keyhole calc."""
from pysecdec_integrals.quark_masses import MC, MB

# the centre of the arc portion of the keyhole
CENTRE = (MC + MB) ** 2

# the radius of the arc portion of the keyhole
RADIUS = 5.0

# the max value of Re(q**2) on the line portion of the keyhole
MAX_RE_QQ = 125.0

# the number of grid points on the line portion of the keyhole
NUM_PTS_LINE = 10

# the number of grid points on the arc portion of the keyhole
NUM_PTS_ARC = 5

# The value of Im(q**2) along the line portion of the keyhole
DELTA = 1e-6

if __name__ == '__main__':
    print(__doc__)
    print(f'MC = {MC}')
    print(f'MB = {MB}')
    print(f'CENTRE = {CENTRE}')
    print(f'RADIUS = {RADIUS}')
    print(f'MAX_RE_QQ = {MAX_RE_QQ}')
    print(f'NUM_PTS_LINE = {NUM_PTS_LINE}')
    print(f'NUM_PTS_ARC = {NUM_PTS_ARC}')
    print(f'DELTA = {DELTA}')
