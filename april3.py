'''1. Function
Given three numbers a, b (a ≤ b) and step. Create an list of evenly spaced elements starting from a to b spaced by step. you have 3 argument:
Input Output
1 5 1 [1, 2, 3, 4, 5]
10 100 20 [10, 30, 50, 70, 90]'''
u = []
x = int(input('Start: '))
y = int(input('End: '))
z = int(input('Step: '))
if x > y and z == abs(z):
	print('Wrong numbers')
elif x < y and z != abs(z):
	print('Wrong numbers')
else:
	for i in range(x,y,z):
		u.append(i)
	print(u)


'''2. List
Write a function. Create the list which elements are products between two neighbours.
Input Output
[3, 7, 12, 5, 20, 0] [21, 84, 60, 100, 0] [1, 1, 4, 32, 6] [1, 4, 128, 192 ]'''
z = []
x = [3, 7, 12, 5, 20, 0]
for i in range(len(x)-1):
	res = x[i] * x[i + 1]
	z.append(res)
print(z)


'''3. New sentence
Given a sentence with missing words and an array of words. Replace all ‘_’ in a sentence with the words from the array.
Input “_, we have a _.”
[“Ashot”, “problem”]
Output: “Ashot, we have a problem.'''
a = ['Ashot', 'problem']
count = 0
u = []

z = '_, we have a _.'
for i in z:
	if i == '_':
		u.append(a[count])
		count += 1 
	else:
		u.append(i)
print(''.join(u))


'''4. sum word
Given a list of strings. Find the strings with maximum and minimum lengths in array. Print the sum of their lengths.
Input: [“anymore”, “raven”, “me”, “communicate”] Output: 13'''

x = ['anymore', 'raven', 'me', 'communicate']
count_max = 0
count_min = 0
for i in x:
	if len(i) > count_max:
		count_max = len(i)
		count_min = len(i)
for i in x:
	if count_min > len(i):
		count_min = len(i)
res = count_min + count_max
print(res)



'''5. find index
Given a list of numbers and a number. Find the index of a first element which is equal to that number. If there is not such a number, that find the index of the first element which is the closest to it. Input Output
[21, -9, 15, 2116, -71, 33], -71 4
[ 36, -12, 47, -58, 148, -55, -19, 10], -56 6'''
u = []
x = [21, -9, 15, 2116, -71, 33]
y = int(input('Number: '))
if y in x:
	z = x.index(y)
	print(z)
else:
	for i in x:
		u.append(abs(i - y))
a = u.index(min(u))
l = x[a]
print(l)


'''6. New Dict
Define a function which can generate a dictionary where the keys are numbers between 1 and N (both included) and the values are square of keys. The function should print the dict.Example :
N =5
{1: 1, 2:4, 3:9, 4:16, 5:25}'''
z = int(input('Number: '))
d = {}
for i in range(1, z + 1):
	d[i] = i ** 2
print(d)

'''7. INVERT Dict
Given an dict. Invert it (keys become values and values become keys).
 If there is more than key for that given value create an list.Input
{ a: ‘1’, b: ‘2’, c: ‘2’ } Output
{ 1: ‘a’, 2: [‘b’, ‘c’] }'''

u = {}
x = {'a':'1','b': '2', 'c': '2'}

for key,value in x.items():
	if value not in u:
		u[value] = [key]
	else:
		u[value].append(key)
print(u)


'''8. FIBONACCI
 Write a function using recursion to find fibonacci numbers:'''

def fibo(n):
	if n <= 1:
		return n
	else:
		return(fibo(n-1) + fibo(n-2))

number = int(input('Number: '))
if number <= 0:
	print('Only positive numbers')
else:
	for i in range(number):
		print(fibo(i))
