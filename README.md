# pySecDec Integral Evaluations for a bc-Diquark Sum-Rules Analysis

The Tarcer basis integrals

- $\mathrm{TBI}(d, q^2, \{\{1, m_c\}, \{1, m_b\}\})$
- $\mathrm{TJI}(d, q^2, \{\{1, m_c\}, \{1, m_b\}, \{1, 0\}\})$
- $\mathrm{TJI}(d, q^2, \{\{2, m_c\}, \{1, m_b\}, \{1, 0\}\})$
- $\mathrm{TJI}(d, q^2, \{\{1, m_c\}, \{2, m_b\}, \{1, 0\}\})$,

where $d = 4 + 2\epsilon$ and $m_c$ & $m_b$ are the charm and bottom quark masses respectively, are evaluated for $q^2$ along a keyhole contour (for $\mathrm{Im}(q^2) \geq 0$) using [pySecDec](https://pypi.org/project/pySecDec/). The paramters that define the keyhole contour are set in `src/keyhole_params.py`:

```python
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
```

## Integral Results

Integral results corresponding to the above settings of the keyhole domain are written to the `data/` directory. There are five files: one for the domain and one for each of the four integrals. All five files are .m files, intended to be read in to a Mathematica notebook.

## Generating New Integral Results

To generate results for keyhole settings other than those given above, start by creating a conda environment:

```bash
$ conda env create --file=environment.yml
```

Then, create the code that pySecDec uses to evaluate integrals:

```bash
$ cd lib
$ python generate_TBI_1_m1_1_m2.py && make -C TBI_1_m1_1_m2 disteval
$ python generate_TJI_1_m1_1_m2_1_0.py && make -C TJI_1_m1_1_m2_1_0 disteval
$ python generate_TJI_2_m1_1_m2_1_0.py && make -C TJI_2_m1_1_m2_1_0 disteval
$ cd ..
```

Finally, change the keyhole settings by directly editing `src/keyhole_params.py`, and run:

```bash
$ python src/main.py
```

The five files in the `data/` directory will be overwritten using the new settings of the keyhole domain.
