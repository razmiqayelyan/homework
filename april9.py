'''1.Max
  Write a python class to find max, min num and and sum in your list:
don’t use max sum and min function'''
import copy

class Number:
	def __init__(self, x):
		self.x = x

	def mecpoqr(self):
		z = 0
		for i in x:
			if i > z:
				z = i
		u = copy.copy(z)
		for i in x:
			if i < u:
				u = i
		return f'amenapoqry: ,{u}, amenamecy, {z}'

x = [123,1231,2143,23,2314]

z = Number
print(z.mecpoqr(x))


'''2.Highest 2
  Write a python class to find two highest values in your dict:'''

class Dic:
	def __init__(self,x):
		self.x = x

	def maxvalue(self):
		l = []
		for i in x.values():
			l.append(i)
			l = sorted(l)
		return l[-1]



x = {'a':-21,'sad':52,'asd':-41}
a = Dic
print(a.maxvalue(x))



'''3.Inheritance
  Write a python class where your child class takes all methods in parent class and print them.'''

class Car:
	def __init__(self, model, speed):
		self.model = model
		self.speed = speed
	def sport(self):
		if self.speed > 120:
			return 'Your car is sportcar'
		else:
			return 'False'

class Auto(Car):
	def printing(self):
		return self.model , self.speed

x = Auto('BMW',130)
print(x.printing())
print(x.sport())


'''4.Rectangle
    Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.'''
class Rectangle:
	def __init__(self, length, width):
		self.l = length
		self.w = width

	def area(self):
		return self.l * self.w
try:
	length = int(input('Lenght:  '))
	width = int(input('Width:  '))
except:
	print('* * * ONLY NUMBERS * * *')
	length = int(input('Lenght:  '))
	width = int(input('Width:  '))

x = Rectangle(length,width)
print(x.area())



'''5.Polymorphism
  Write a python class where we use polymorphism: Example:
a.country() - Erevan
b.country() - Paris'''

class Armenia:
	def country():
		return 'Yerevan'
	def Check():
		print('Hello from Armenia')
		return x.country()

		
class UAE:
	def country():
		return 'Abu-Dhabi'
	def Check():
		print('Hello from UAE')
		return y.country()
		
x = Armenia
print(x.Check())
y = UAE
print(y.Check())



























