# Python implementation of
# Archimedes' method for
# estimating pi
class arch:
	__a0 = 2*(3**0.5)
	__b0 = 3
	
	def __an(self, n):
		if (n == 0):
			return arch.__a0
		else:
			return (2*self.__an(n-1)*self.__bn(n-1))/(self.__an(n-1)+self.__bn(n-1))
	
	def __bn(self, n):
		if (n == 0):
			return arch.__b0
		else:
			return (self.__an(n)*self.__bn(n-1))**0.5

	def arch_mean_iter(self, n):
		return self.__an(n)

a = arch()
a.arch_mean_iter(4.0)

