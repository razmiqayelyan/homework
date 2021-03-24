import json
'''1. Write a Python program to add info in JSON file about you.'''
x = input('Information:  ')
with open('Info.json', 'w') as file:
	json.dump(x, file)

'''2. Write a Python program to get info in JSON file about you.'''

with open('Info.json', 'r') as file:
	print(json.load(file))

'''3. Write a Python program to check if your json file have this info.'''
z = input('-->  ')
file = open('Info.json')
json_data = json.load(file)
for data in json_data:
	if data == z:
		print(data)
	

	







