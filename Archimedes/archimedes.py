# Python implementation of
# Archimedes' method for
# estimating pi
import math
class arch:
	__a0 = 2*(3**0.5)
	__b0 = 3
	

	def arch_mean_iter(self, n):
		an = arch.__a0
		bn = arch.__b0

		for i in range(n):
			an = (2*an*bn)/(an + bn)
			bn = (an * bn)**0.5
			print "an = ", an, "bn = ", bn
			print "error = ", abs(math.pi - bn)
			

a = arch()
a.arch_mean_iter(10)

