# Makefile for pysecdec_integrals
#
# This Makefile is used to generate the pySecDec integral libraries for
# three dimensionally-regularized integrals needed for evaluating the
# bc-diquark two-point function.

.PHONY: all clean generate

all: clean generate

# Remove all generated files.
clean:
	rm -rf TBI_1_m1_1_m2 TJI_1_m1_1_m2_1_0 TJI_2_m1_1_m2_1_0

# Generate the three integral libraries.
generate:
	$(MAKE) clean
	python -m pysecdec_integrals.generate_TBI_1_m1_1_m2
	python -m pysecdec_integrals.generate_TJI_1_m1_1_m2_1_0
	python -m pysecdec_integrals.generate_TJI_2_m1_1_m2_1_0
	make -C TBI_1_m1_1_m2 disteval
	make -C TJI_1_m1_1_m2_1_0 disteval
	make -C TJI_2_m1_1_m2_1_0 disteval
