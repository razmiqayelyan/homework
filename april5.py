'''1. Odd
Write a recursive function to determine whether 
all digits of the number are odd or not.
Input Output 
4211133 false
7791 true 5 true'''

def kent(tiv):
	n = 1
	tiv = str(tiv)
	if int(tiv[len(tiv) - n]) % 2 == 0:
		return False
	elif n == len(tiv):
		return True
	else:
		n += 1
		return kent(int(tiv[len(tiv) - n]))

print(kent(7791))


 ###  ARANC REKURSIAI  ###
# def kent(tiv):
# 	z = True
# 	for i in tiv:
# 		if int(i) % 2 == 0:
# 			z = False
# 	return z
# try:
# 	x = input('Numbers:  ')
# 	for i in x:
# 		if i.isalpha() or i == ' ':
# 			raise ValueError
# except:
# 	print('\t*** Only Numbers *** ')
# 	x = input('Numbers:  ')
# print(kent(x))


'''2. Threading
 Write a python function all even number in 10.000 use threading and print time.'''

import threading
import time
def zuyg(start, end):
	with open('even.txt', 'w') as kent:
		for i in range(start, end):
			if i % 2 == 0:
				kent.write(str(f'{i} , '))
start_time = time.time()
t1 = threading.Thread(target=zuyg,args=(2,5002))
t2 = threading.Thread(target=zuyg,args=(5002,10000))
t1.start()
t2.start()
t1.join()
t2.join()
zuyg(1, 10000)
print('Time:',time.time() - start_time )

'''3. Numbers
Given N number. Write a recursive function that should print from 1 to N numbers.
Input Output
5 1, 2, 3, 4, 5'''
def rec(n):
	if n == 1:
		return n
	else:
		print(n)
		return rec(n-1)

print(rec(10)) 


''' 4. Longest Word
Write a python program to find the longest word from the file content.
Need to use <try-except> block in the file reading process and print time. example
 1. 2. 3. 4. 5. 6. 7.
try:
with open("filename.txt") as file: some code
except:
do something
Function call: find_long_word("filename.txt") Function output: "LongestWord" '''


with open('longest.txt') as file:
	x = file.read()
	z = ''
	u = []
	v = []
	for i in x.split():
		u.append(i)
	for i in u:
		if len(i) > len(z):
			z = i
	for i in u:
		if len(i) == len(z) and i not in v:
			v.append(i)
	if len(v) > 1:
		print('LongestWords:', v)
	else:	
		print('LongestWord:', z)
