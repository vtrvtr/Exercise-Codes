 # [2015-03-11] Challenge #205 [Intermediate] RPN
import re
import string
from Queue import Queue as Q

notations = '''      0+1
      20-18
       3               x                  1
       100    /                4
       5000         /  ((1+1) / 2) * 1000
       10 * 6 x 10 / 100
       (1 + 7 x 7) / 5 - 3
      10000 / ( 9 x 9 + 20 -1)-92
      4+5 * 333x3 /      9-110
       0 x (2000 / 4 * 5 / 1 * (1 x 10)) '''


single_notations = [notation.replace(' ', '') for notation in notations.split('\n')]
single_notations2 = [notation.replace('x', '*') for notation in single_notations]
def parsing(notation):
    parsed = []
    for _ in notation:
        if _ is not ' ':
            parsed.append(_)
    return parsed

def parsing2(math_string):
    final_list = []
    digit_list = []
    c = 0

    while c < len(math_string):
        if math_string[c] in string.digits:
            while math_string[c] in string.digits:
                digit_list.append(math_string[c])
                c += 1
            final_list.append(''.join(digit_list))
            digit_list = []

        if math_string[c] in string.punctuation:
            final_list.append(math_string[c])
            c += 1
    return final_list


lol = single_notations2[6]
print eval(lol)
# def number_separe(notation):
#     n_queue = Q()
#     numbers = [number for number in re.split('[ -/+x]', notation) if number is not '']
#     for number in numbers:
#         n_queue.put(number)
#     return n_queue

    
# def symbol_separe(notation):
#     s_queue = Q()
#     symbols = [symbol for symbol in re.findall('[()+/x-]', notation)]
#     for symbol in symbols:
#         s_queue.put(symbol)
#     return s_queue


# def convert_polish(numbers, symbols):

#     while not numbers.empty():
#         symbol = symbols.get()
#         if symbol in '()':
#             pass
#         else:
#             _ = [number.get() for i in xrange(2)]

#     return ' '.join(rpn)

def test():
    for notation in single_notations:
        pass
