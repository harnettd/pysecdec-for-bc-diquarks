# pySecDec Integral Evaluations for a bc-Diquark Sum-Rules Analysis

The Tarcer basis integrals

- $\mathrm{TBI}(d, q^2, [[1, m_c], [1, m_b]])$
- $\mathrm{TBI}(d, q^2, [[2, m_c], [1, m_b]])$
- $\mathrm{TBI}(d, q^2, [[1, m_c], [2, m_b]])$
- $\mathrm{TJI}(d, q^2, [[1, m_c], [1, m_b], [1, 0]])$
- $\mathrm{TJI}(d, q^2, [[2, m_c], [1, m_b], [1, 0]])$
- $\mathrm{TJI}(d, q^2, [[1, m_c], [2, m_b], [1, 0]])$,

where $d = 4 + 2\epsilon$ and $m_c$ & $m_b$ are the charm and bottom quark masses respectively, are evaluated for $q^2$ along a keyhole contour (for $\mathrm{Im}(q^2) \geq 0$) using [pySecDec](https://pypi.org/project/pySecDec/). The parameters that characterize the keyhole contour are defined between `pysecdec_integrals/quark_masses.py`, 

```python
"""Bottom and charm quark masses."""
MC = 1.095    # charm quark mass
MB = 4.47521  # bottom quark mass
```

and `pysecdec_integrals/keyhole_params.py`,

```python
# the centre of the arc portion of the keyhole
CENTRE = (MC + MB) ** 2

# the radius of the arc portion of the keyhole
RADIUS = 15.

# the max value of Re(q**2) on the line portion of the keyhole
MAX_RE_QQ = 150.

# the number of grid points on the line portion of the keyhole
NUM_PTS_LINE = 250

# the number of grid points on the arc portion of the keyhole
NUM_PTS_ARC = 50

# The value of Im(q**2) along the line portion of the keyhole
DELTA = 1e-12
```

## Integral Results

Integral results corresponding to the above settings of the keyhole domain are written to the `data/` directory. There are several files: one for the domain and one for each of the integrals. All files are .m files, intended to be read in to a Mathematica notebook.

## Generating New Integral Results

To generate results for keyhole settings other than those given above, start by creating and activating a conda environment:

```bash
$ conda env create --file=environment.yml
$ conda activate pysecdec
```

Then, generate the libraries that pySecDec uses to evaluate integrals:

```bash
$ make
```

Optionally, run all available unittests:
```bash
$ python -m unittest discover
```

Finally, adjust the quark masses and keyhole parameters as needed by directly editing `pysecdec_integrals/quark_masses.py` and `pysecdec_integrals/keyhole_params.py`, and run:

```bash
$ python -m pysecdec_integrals.integrate
```

The five files in the `data/` directory will be overwritten with integral results corresponding to the new settings of the quark masses and keyhole domain.
