def print_modulo(n , d):
	if d>n:
		return n
	elif n>d:
		sum = n/d
		rem = n - (int(sum) * d)
	return rem
print(print_modulo(10,6))
