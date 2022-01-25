def addStrNums(num1, num2):
	out = ''
	try:
	  out = f"{int(num1) + int(num2)}"
	except ValueError:
		out = '-1'
	finally:
		return out

print(addStrNums('55','3'))