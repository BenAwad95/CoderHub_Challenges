import re
def postFix(expr):
	numbers = re.findall('\d+', expr)
	op = re.findall('[+-/*%]', expr)

	expression = ''
	for n, o in zip(numbers, op):
		expression+=n
		expression+=o
	expression+= numbers[-1]

	return eval(expression)

# print(postFix('4 1 - 2 *'))

import re
def postFix(expr):
	numbers = re.findall('\d+', expr)
	op = re.findall('[+-/*%]', expr)

	equl = eval(f"{numbers[0]}{op[0]}{numbers[1]}")
	numbers.pop(0)
	numbers.pop(0) # BE SMART AND THINK WHY I DID IT THAT.
	op.pop(0)
	while len(op) != 0:
		equl = eval(f"{equl}{op[0]}{numbers[0]}")
		numbers.pop(0)
		op.pop(0)
	return int(equl)

print(postFix('2 3 * 1 - 5 /'))


	

