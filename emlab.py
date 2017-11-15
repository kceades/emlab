import numpy as np

def calculate(I,V,r,delta_r=None):
	"""
	Calculates the e/m ratio

	inputs:
	:I: Current to the Helmholtz coils in Amps
	:V: Voltage to the electrons in Volts
	:r: Measured radius in meters
	:delta_r: Uncertainty in measured radius

	return:
	the e/m ratio if delta_r is none
	[em ratio, delta em ratio] if delta_r is not None

	Note: divide by 1e11 after the calculation if you want to see single digits
	"""
	N = 130
	R = 0.15
	B = 9.0e-7*N*I/R
	em = 2*V/(r**2*B**2)
	if delta_r is not None:
		delta_em = 4*V*delta_r/(r**3*B**2)
		return [em,delta_em]
	return em