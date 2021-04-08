''' 1.CALCULATOR '''
class calculator():
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def plus(self):
		return self.a + self.b
	def minus(self):
		return self.a - self.b
	def angam(self):
		return self.a * self.b
	def bajanac(self):
		return self.a / self.b



try:
	a = int(input('Number 1: '))
	b = int(input('Number 2: '))
except:
	print('Only Numbers')
	a = int(input('Number 1: '))
	b = int(input('Number 2: '))
resultat = calculator(a,b)
x = ['+','-','/','*']
while True:
	z = input('+ - / * \n')
	if z in x:
		break
	else:
		print('Check one of this simvoles:')
if z == '*':
	print(resultat.angam())
elif z == '+':
	print(resultat.plus())
elif z == '-':
	print(resultat.minus())
else:
	print(round(resultat.bajanac(), 2))

''' 2.CAR 
	Create a class for Car and Person '''

class Car:
	def __init__(self, mark, speed, color):
		self.mark = mark
		self.speed = speed
		self.color = color

	def xadavik(self):
		if self.speed > 220:
			return f'Dzer {self.mark} modeli {self.color} meqenan hamarvum e sportain'
		else:
			return f'Dzer {self.mark} modeli {self.color} meqenan sportain chi'
mark = input('Mark: ')
try:
	speed = int(input('Speed: '))
except:
	print('Only Numbers in Speed')
	speed = int(input('Speed: '))
color = input('Color: ')
x = Car(mark,speed,color)
print(x.xadavik())


''' CHANGE.
	Create a class Change:You have 3 
	methods in your class:
	USD --- EUR
	USD --- AMD
	USD --- RUR '''

class Change():
	def __init__(self, usd):
		self.usd = usd 
	def amd(self):
		return self.usd * 536
	def eur(self):
		return self.usd * 1.19
	def rur(self):
		return self.usd * 77
dollar = int(input('Dollar: '))
a = Change(dollar)
def valute():
		x = input('eur amd rur\n').lower()
		if x == 'eur':
			return a.eur()
		elif x == 'rur':
			return a.rur()
		elif x == 'amd':
			return a.amd()
		else:
			return f'Wrong input {x}'
print(valute())




































