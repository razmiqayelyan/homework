'''Min
Create a python class which given an list of integers, find the maximal absolute difference between any two of its adjacent elements.
Example
For inputArray = [2, 4, 1, 0], the output should be output = 3.'''

a =  [2, 4, 1, 0]
z = None
for i in range(len(a)-1):
	res = a[i] - a[i + 1]
	if z == None:
		z = res
	elif res > z:
		z = res
print(z)
