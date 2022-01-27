singles = ["zero","one","two","three","four","five","six","seven","eight","nine"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

def numToEng(n):
	out = ''
	# singles case
	if 0 <= n <= 9:
		out = singles[n]

	# teens case
	if 10 <= n <= 19:
		out = teens[n%10]

	# tens case
	if 20 <= n <= 99:
		# number string
		ns = str(n)
		fisrt_part = tens[int(ns[0])]
		if ns[1] == '0':
			out = fisrt_part
		else:
			second_part = singles[int(ns[1])]
			out = f"{fisrt_part}-{second_part}"	

	# hundred and up to 999
	if 100 <= n <= 999:
		ns = str(n)
		fisrt_part = singles[int(ns[0])]
		if ns[1:] == '00':
			out = f"{fisrt_part} hundred"
		else:
			second_part = singles[int(ns[-1])]
			out = f"{fisrt_part} hundred {numToEng(int(ns[1:]))}"
	return out.strip()


# print(numToEng(202))

"""Given an int32 number, print it in English."""
def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))

import inflect
p = inflect.engine()
n=999

print(numToEng(50))
print(int_to_en(555))
