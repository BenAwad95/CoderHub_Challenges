# TODO replace all space in input string into '#'

def hasSpace(string):
	string = string.strip()
	string = string.replace(' ', '#')
	return string

print(hasSpace('Goood Mornning')) 