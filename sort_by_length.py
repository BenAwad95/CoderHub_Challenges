def sortByLength(txt):
	words = txt.split()
	words.sort(key=len)
	return ' '.join(words)


print(sortByLength('My name is abdullah'))