def nod(x, y):
	while x != y:
		if x > y:
			x = x - y
		else:
			y = y - x
	return x
while True:
	try:
		a, b = map(int, input().split())
		print(nod(a, b))
	except:
		break
