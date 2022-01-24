def cap_space(txt):
  out = ''
  for l in txt:
    if l.isupper():
      out += ' '
    out += l
  return out.strip().lower()

print(cap_space('ILikeYou'))