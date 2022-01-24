def oddsVsEvens(num):
  # write your code here
  num_list = list(map(int, list(str(num))))
  odds = sum(list(filter(lambda x: x%2 != 0, num_list)))
  evens = sum(list(filter(lambda x: x%2 == 0, num_list)))
  if odds == evens:
    return 'equal'
  return 'odds' if odds > evens else 'evens'

print(oddsVsEvens(344))