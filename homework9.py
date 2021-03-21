'''1.Create 5 file (.txt) and write messages in them.'''
with open('file1.txt', 'w') as file1:
	login = input('Login: ')
	file1.write(login)
with open('file2.txt', 'w') as file2:
	login = input('Password: ')
	file2.write(login)
with open('file3.txt', 'w') as file3:
	login = input('email: ')
	file3.write(login)
with open('file4.txt', 'w') as file4:
	login = input('Name/Surname: ')
	file4.write(login)
with open('file5.txt', 'w') as file5:
	login = input('ser: ')
	file5.write(login)


'''2. Write a Python program to read first n lines of
a file.'''
with open('file2.txt', 'r') as file2:
	toxer = int(input('Lines:  '))
	for i in range(toxer):
		print(file2.readline(), end='')

'''3.Write a Python program to append text to a file and display the text.'''
with open('file2.txt', 'a') as file2:
	x = input('Text: ')
	file2.write(x)
	print('text' ,x)
with open('file2.txt', 'r') as file2:
	z = file2.read()
	print('file:',z)

'''4.Write a python program to find the longest words.'''
with open('file2.txt', 'r') as file2:
	z = '' 
	x = file2.read()
	for i in x.split():
		if len(i) > len(z):
			z = i
	print(z)

'''5.Write a python program to find numbers in txt.''' 
with open('file2.txt', 'r') as file2:
	z = []
	for i in file2.read():
		for x in i:
			if x.isdigit():
				z.append(x)
	print(z)


'''6.Write a python program to get login and password.'''
with open('file1.txt', 'w') as file1:
	login = input('Login: ')
	file1.write(login)
	print('Your Login is:', login)
with open('file2.txt', 'w') as file2:
	login = input('Password: ')
	file2.write(login)
	print('Your password is:', login)