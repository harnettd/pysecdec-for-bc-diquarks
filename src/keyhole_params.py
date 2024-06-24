"""
Parameters needed to define a keyhole domain.
"""
# quark masses
MC = 1.27  # charm
MB = 4.18  # bottom

# the centre of the arc portion of the keyhole
CENTRE = (MC + MB) ** 2

# the radius of the arc portion of the keyhole
RADIUS = 5.0

# the max value of Re(q**2) on the line portion of the keyhole
MAX_RE_QQ = 125.0

# the number of grid points on the line portion of the keyhole
NUM_PTS_LINE = 300

# the number of grid points on the arc portion of the keyhole
NUM_PTS_ARC = 25

# The value of Im(q**2) along the line portion of the keyhole
DELTA = 1e-6


if __name__ == '__main__':
    print(__doc__)
