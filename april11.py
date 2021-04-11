'''1. century
Create a class which given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
For year = 1900, the output should be = 19'''
class Year:
	def __init__(self, y):
		self.y = y

	def dar(self):
		if  int(self.y) % 100 == 1:
			return int(self.y) // 100 + 1
		else:
			return int(self.y) // 100
x = Year('2000')
print(x.dar())

'''2. Palindrome
Create a class given the string, check if it is a palindrome. word should be lowercase and 1 ≤ inputString.length ≤ 105 Example
For inputString = "aabaa", the output should be true;
For inputString = "abac", the output should be false; For inputString = "a", the output should be true.
'''

class Palindrome:
	def __init__(self,bar):
		self.b = bar
	def yesno(self):
		if self.b == self.b[::-1]:
			return f'Yes "{self.b}" is Palindrome'
		else:
			return 'No'
z = input('Bar: ').lower()
x = Palindrome(z)
print(x.yesno())


'''3. Largest
Create a Class which given an list of integers, find the pair of adjacent elements that has the largest product and return that product.
For inputList = [3, 6, -2, -5, 7, 3], the output should be = 21.'''

inputList = [3, 6, -2, -5, 7, 3]
z = []
for i in range(len(inputList) - 1):
	res = inputList[i] * inputList[i+1]
	z.append(res)
print(max(z))

'''4. find highest word
Create a class which given a list of strings, return another list containing all of its longest strings.
Example
For inputList = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputList) = ["aba", "vcd", "aba"].'''

inputList = ["aba", "aa", "ad", "vcd", "aba"]
class Bar:
	def __init__(self,inputList):
		self.inputList = inputList
	def erkary(self):
		u = ''
		z = []
		for i in self.inputList:
			if len(i) > len(u):
				u = i
		z.append(u)
		self.inputList.remove(u)
		for i in self.inputList:
			if len(i) == len(u):
				z.append(i)
		return z
x = Bar(inputList)
print(x.erkary())


'''5. Lucky
Ticket numbers usually consist of an even number of digits.A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.Given a ticket number n, determine if it's lucky or not. Example For n = 1230, the output should be
Lucky(n) = true;
For n = 123021,
the output should be Lucky(n) = false'''

n = '421232'
class Bilet:
	def __init__(self,hamar):
		self.hamar = hamar
	def winlose(self):
		count = 0
		z = []
		for i in range(0 ,len(self.hamar) -1, 2):
		    res = int(self.hamar[i]) + int(self.hamar[i+1])
		    if count == 0:
		    	z.append(res)
		    	count += 1
		    if res not in z:
		    	return 'LOSE'		    
		return 'WIN'
a = Bilet(n)
print(a.winlose())


'''6. List sort
Create a class: Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!
Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''
a = [-1, 150, 190, 170, -1, -1, 160, 180]
class Tree:
	def __init__(self, a):
		self.a = a
	def height(self):
		b = []
		z = []
		for i in self.a:
			if i != -1:
				b.append(i)
		b = sorted(b)
		n = 0
		for i in self.a:
			if i == -1:
				z.append(i)
			else:
				z.append(b[n])
				n += 1
		return z
x = Tree(a)
print(x.height())


'''7. Weight
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.
Example For a = [50, 60, 60, 45, 70], the output should be alternating Sums(a) = [180, 105].'''
a = [50, 60, 60, 45, 70]
class Team:
	def __init__(self, a):
		self.a = a
	def teams(self):
		tema1 = []
		team2 = []
		for i in range(0,len(self.a),2):
			tema1.append(self.a[i])
		for i in range(1,len(self.a), 2):
			team2.append(self.a[i])
		return f'First Team {sum(tema1)}\nSecons Team {sum(team2)}'
		

x = Team(a)
print(x.teams())

