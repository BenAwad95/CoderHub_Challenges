

def merge_sort(arr1, arr2):
	out = (arr1 + arr2)
	out.sort()
	return out

print(merge_sort([1,2,3], [0,-1,-5]))