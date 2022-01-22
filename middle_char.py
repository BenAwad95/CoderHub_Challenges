def middle_char(word):
	if len(word)%2 == 0:
		m = int(len(word) / 2)
		out = word[m-1:m+1]
	else:
		m = int((len(word)-1) /2)
		out = word[m]
	return out

print(middle_char('arrt'))