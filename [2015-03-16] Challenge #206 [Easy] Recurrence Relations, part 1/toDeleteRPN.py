import string
import operator
ops = {'+': operator.add, '-': operator.sub,
       '*': operator.mul, '/': operator.div}


import string, operator
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
while True:
  try:
    st = []
    print st
    for tk in string.split(raw_input()):
      if tk in ops:
        print tk
        y,x = st.pop(),st.pop()
        z = ops[tk](x,y)
      else:
        z = int(tk)
      st.append(z)
    assert len(st)<=1
    if len(st)==1: print(st.pop())
  except EOFError:  break