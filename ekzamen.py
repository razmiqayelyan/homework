'''Difficulty: Easy
The doctors and the scientists are found out that you can learn about your illness coronavirus  from home by the following formula. If you duplicate your  body temperature by Celsus with the number of pi and round up to the nearest whole number and if it is between the intervals of 120 to 128  so you have coronavirus otherwise no. 
'''
# import math
# class Corona:
# 	def __init__(self,celsus):
# 		self.c = celsus
# 	def corona(self):

# 		res = self.c * math.pi
# 		if math.ceil(res) >= 120 and math.ceil(res) <= 128:
# 			return 'You Have coronavirus'
# 		else:
# 			return 'Everything is ok'

# z = Corona(36.6)
# print(z.corona())


'''The english scientists found out that each english letter has its corresponding numbers. And they create a chart where: 1 = a, j, s  2 = b, k, t  3 = c, l, u  4 = d, m, v   5 = e, n, w   6 = f, o, x 
7 = g, p, y   8 = h, q, z   9 = i, r   and you will know if your name is widespread or no when you
square root your name number and  arranging number in ascending order is less than 5:
'''
# first = ['a', 'j', 's']
# second = ['b', 'k', 't']
# erord = ['c', 'l', 'u']
# chorord = ['d', 'm', 'v']
# hingerord = ['e', 'n', 'w'] 
# vecerord = ['f', 'o', 'x']
# yoterord = ['g', 'p', 'y']
# uterord = ['h', 'q', 'z']
# innerord = ['i', 'r']

# x = input('Name:  ').lower()
# class Anun:
# 	def __init__(self,x):
# 		self.x = x
# 	def superstar(self):
# 		res = 0
# 		for i in self.x:
# 			if i in first:
# 				res += 1
# 			elif i in second:
# 				res += 2
# 			elif i in erord:
# 				res += 3
# 			elif i in chorord:
# 				res += 4
# 			elif i in hingerord:
# 				res += 5
# 			elif i in vecerord:
# 				res += 6
# 			elif i in yoterord:
# 				res += 7
# 			elif i in uterord:
# 				res += 8
# 			elif i in innerord:
# 				res += 9
# 		u = math.sqrt(res)
# 		if u < 5:
# 			return f'Your name {x} is widespread,\ntotal- {res}'
# 		else:
# 			return f"Your name {x} is not widespread,\ntotal- {res}"


# z  = Anun(x)
# print(z.superstar())

'''You are Harry Potter and you fight with Lord Voldemort in order to protect your friends.
You should use magic words for winning him. You both use the following magic words
during fighting:  Avada Kedavra,  Crucio, Imperio  . You get 1 point when your word corresponds to his, otherwise you lose 1 point. You have three attempts and you will
become a winner if  you have 2 corresponding words.
'''
import random


total = 0
x =  ['Avada Kedavra',  'Crucio', 'Imperio']
class Magic:
	def __init__(self,x,total):
		self.x = x
		self.total = total
	def game(self):
		for i in range(3):
			pc = random.choice(self.x)
			print(pc)
			user = input('Enter your choice:\n"Avada Kedavra", "Crucio", "Imperio"\n ').title()
			if pc == user:
				self.total += 1
				print(f'* * * * * You are right,you have {2-i} chance * * * * *')
			else: 
				self.total -+ 1
				print(f'* * * * * Wrong,you have {2-i} chance * * * * *')
		if self.total >= 2:
			return ' - - - You are Win - - - '
		else:
			return ' - - - You are Lose - - - '
player = Magic(x,total)
print(player.game())