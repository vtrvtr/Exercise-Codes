 #[2015-03-16] Challenge #206 [Easy] Recurrence Relations, part 1
ipt = '*2)+1'

def recursive(n, expression):
    result = '({}{}'.format(n, expression)
    print result
    return eval(result)



def call_many_times(how_many, expression, first_term = 0):
   return first_term if how_many == 0 else call_many_times(how_many-1, expression, recursive(first_term, ipt)) 


print call_many_times(3, ipt)
