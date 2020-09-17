def my_func():
	x = {'a':1, 'b':2}
	y = {'b':3, 'c':4}
	a = [{*x, *y}]
	return a, {**x, **y}
b = my_func()
print(type(b))