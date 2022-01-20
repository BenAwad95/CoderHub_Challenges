def array_root(arr):
	# write your code here
	return list(map(lambda x: pow(x, 0.5), arr))


print(array_root([9, 16, 25]))