'''1. Dict
You have two list convert it in dictionary and add in (mydict.txt) and show result:
for example: input :
first = [‘Ani’, ‘Jessy’, ‘Ben’]
second = [1,2,3]
my_dict = {1 : “Ani” , 2: “Jessy”, 3: “Ben”}'''
first = ['Ani', 'Jessy', 'Ben']
second = [1,2,3]
mydict = {}
for a,b in zip(first,second):
	mydict[b] = a
print(mydict)

'''2. Json
 Create json file and save them lyrics (song) and print in cmd word this song.'''
import json
text = {'Miyagi':'Top','Andy':'Best'}
with open('info.json', 'w') as file:
	json.dump(text, file)
with open('info.json', 'r') as file:
	print(json.load(file))

'''3. Function
Write a python program which have one input an integer, representing the sum of all the multiples of 3 and 5 below the given input. and save this result in json file.
for example:
input 10 (3, 5, 6 and 9)
output:23'''
z = []
try:
	x = int(input('Number:  '))
except:
	print('Only numbers')
	x = int(input('Number:  '))

for i in range(x):
	if i % 3 == 0 or i % 5 == 0:
		z.append(i)
print(sum(z))

'''4. Vowels
Write a program that takes in a string as input, counts and outputs the number of vowels. And add result in json file.
for example: input: test output: 1'''
import json
x = ['A', 'E', 'I', 'O', 'U', 'Y']
z = input('-->  ').upper()
total = 0
for i in z:
	if i in x:
		total += 1
print(total)
with open('Info.json', 'w') as file:
	json.dump(total,file)	

'''5. text
You have text.txt file and contains such text:
Another pause and more eying and siding around each other
You can create one dict where you have. ‘’another’’:1
‘’and’’:2 ................'''
with open('teqsta.txt', 'r') as file:
	x = str(file.read())
	z = {}
	u = 1
	for r in x.split():
		print(r)
		z[r] = u 
		u += 1
print(z)

'''6. NEw list
Write a python function which get a new list from a given list, consisting of the first repeating elements.
my_list = [“a”,”b”,”a”,”c”,”b”] output “a”,”b”,”c”'''
z = []
my_list = ['a','b', 'a', 'c', 'b']
for i in my_list:
	if i not in z:
		z.append(i)

'''7. How much
You have word.txt file and in them you have one story.
Write a Python function that accepts this story and calculate the number of uppercase letters and lowercase letters.'''
with open('news.txt','r') as file:
	mecatar = 0
	poqratary = 0
	x = file.read()
	for i in x:
		if i == i.upper():
			mecatar += 1
		elif i == i.lower():
			poqratary += 1

print('Mecatar-->' ,mecatar, 'Poqratar-->',poqratary)
