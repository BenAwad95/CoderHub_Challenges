# TODO convert oct number to hex number

def oct_to_hex(oct):
	# write your code here
	n = int(f"0o{oct}", 8)
	h = hex(n)
	return h[2:].upper()

print(oct_to_hex(234))