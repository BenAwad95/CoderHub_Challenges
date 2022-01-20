def unique(arr):
  # write your code here
  return list(filter(lambda x: arr.count(x) == 1, arr))

print(unique([1,1,2,3]))