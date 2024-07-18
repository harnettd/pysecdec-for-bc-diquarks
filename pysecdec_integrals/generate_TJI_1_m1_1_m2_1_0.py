"""
A pySecDec generate file for the dim-reg integral

	TJI[d, q**2, {{1, m1}, {1, m2}, {1, 0}}] 

where d = 4 + 2*eps, q**2 is external (Minkowski) squared-momentum,
and m1 and m2 are propagator masses.
"""
from sympy import symbols

import pySecDec as psd

from pysecdec_integrals.quark_masses import MC, MB
from pysecdec_integrals.get_additional_prefactor import\
	get_additional_prefactor as gap

if __name__ == '__main__':

	eps = symbols('eps')
	dimensionality = 4 + 2 * eps
	additional_prefactor =\
		gap.get_additional_prefactor(dimensionality, num_loops=1, masses=[MC, MB])

	li = psd.LoopIntegralFromGraph(
		internal_lines=[
			['m1', [1, 2]], 
			['m2', [1, 2]], 
			[0, [1, 2]] 
		],
		external_lines=[ 
			['p1', 1], 
			['p2', 2]
		],
		replacement_rules=[
			('p1*p1', 'qq'),
			('p2*p2', 'qq'),
			('p1*p2', '-qq'),
			('m1**2', 'm1m1'),
			('m2**2', 'm2m2')
		],     
		regulator=eps,
		dimensionality=dimensionality,
		powerlist=[1, 1, 1]
	)

	kinematics_symbols = ['qq']
	mass_symbols = ['m1m1', 'm2m2']

	psd.loop_package(
		name='TJI_1_m1_1_m2_1_0',
		loop_integral=li,
		complex_parameters=kinematics_symbols,
		real_parameters=mass_symbols,
		additional_prefactor=additional_prefactor,

		# The order of the epsilon expansion 
		requested_orders = [2],

		# The optimization level to use in FORM (can be 0, 1, 2, 3, 4)
		form_optimization_level = 2,

		# the WorkSpace parameter for FORM
		form_work_space = '100M',

		# The method to use for sector decomposition:
		# 	'iterative' or 'geometric' or 'geometric_ku'
		decomposition_method = 'iterative',
			
		# If you choose the decomposition_method 'geometric[_ku]',
		# but 'normaliz' is not in your $PATH, then set the path 
		# to the 'normaliz' command-line executable here:
		# normaliz_executable='/home/derek/normaliz-3.10.3/normaliz'
	)
