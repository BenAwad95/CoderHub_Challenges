import re
def first_n_vowels(phrase, n):
  # write your code here
  out = re.findall('[aeiouAEIOU]', phrase)
  try:
    check = out[n-1]
    return ''.join(out[:n])
  except:
    return 'invalid'

print(first_n_vowels('ProgrAmmEr', 3))