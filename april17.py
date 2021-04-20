from functools import wraps
import time

def time_test(func):
	@wraps(func)
	def times():
		start = time.time()
		func()
		print(time.time()-start)
	return times


@time_test
def even():
	print('even')
	c = []
	for i in range(10000000):
		if i % 2 == 0:
			c.append(i)




@time_test
def test2():
	print('tets2')
	time.sleep(0.1)
	return 6+6

if _name_ == "_main_":
	even()
	test2()
	print(even.__name__)



def res(func:callable):

	@wraps(func)
	def test(*args) -> int:
		print('Result')
		return func(*args)
	return test	

@res
def testing(a:int,b:int) -> int:
	return a + b

print(testing('12','5'))