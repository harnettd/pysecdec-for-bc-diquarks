# Makefile for pysecdec_integrals
#
# This Makefile is used to generate the pySecDec integral libraries for
# the dimensionally-regularized integrals needed for evaluating the
# bc-diquark two-point function.

.PHONY: all clean generate

all: clean generate

# Remove all generated files.
clean:
	rm -rf TBI_1_m1_1_m2 TBI_2_m1_1_m2 TJI_1_m1_1_m2_1_0 TJI_2_m1_1_m2_1_0

# Generate the three integral libraries.
generate:
	$(MAKE) clean
	python -m pysecdec_integrals.generate_TBI_1_m1_1_m2
	python -m pysecdec_integrals.generate_TBI_2_m1_1_m2
	python -m pysecdec_integrals.generate_TJI_1_m1_1_m2_1_0
	python -m pysecdec_integrals.generate_TJI_2_m1_1_m2_1_0
	$(MAKE) -C TBI_1_m1_1_m2 disteval
	$(MAKE) -C TBI_2_m1_1_m2 disteval
	$(MAKE) -C TJI_1_m1_1_m2_1_0 disteval
	$(MAKE) -C TJI_2_m1_1_m2_1_0 disteval
