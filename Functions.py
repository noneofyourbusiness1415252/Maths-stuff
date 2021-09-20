from math import log


def Prime(n):
	if n == 2 or n == 3:
		return True
	if n < 2 or n % 2 == 0:
		return False
	if n < 9:
		return True
	if n % 3 == 0:
		return False
	r = int(n ** 0.5)
	f = 5
	while f <= r:
		if n % f == 0:
			return False
		if n % (f + 2) == 0:
			return False
		f += 6
	return True


def Power(n, p):
	return n ** (1 / p) == int(n ** (1 / p))


def SquareorCube(n):
	if Power(n, 2) and Power(n, 3):
		return "both"
	elif Power(n, 2):
		return "square"
	elif Power(n, 3):
		return "cube"
	else:
		return "neither"
