def f(num):
	factorial = 1
	if num < 0:
		print('Not exits negative numbers')
	elif num == 0:
		print('The factorial of 0 is 1')
	else:
		for i in range(1, num+1):
			factorial *= i
		print(num, '-i factorialy havasar e', factorial)

def glan(r,h):
	pi = 3.14
	V = pi * (r ** 2) * h
	A = (2 * pi *r * h) + (2 * pi * (r**2))
	return f'V-n havasar e {V},A-n havasar e {A}'

def gund(r):
	pi = 3.14
	V = 4/3 * pi * (r ** 3)
	A = 4 * pi * (r ** 2)
	return f'Volume-->{V}, Surface Area-->{A}'

def radian(x):
	pi = 3.14
	count = pi/180 * x
	return count

def parz(x):
	z = []
	for i in range(x):
		if i % 2 != 0:
			z.append(i)
	return z


