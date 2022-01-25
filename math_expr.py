import re
def math_expr(expr):
  math_expr = re.findall('^\d+[+-/*%]\d+$', expr)
  return True if len(math_expr) else False


print(math_expr('3+f'))