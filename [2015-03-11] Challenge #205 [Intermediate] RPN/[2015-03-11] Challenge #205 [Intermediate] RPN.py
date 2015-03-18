 # [2015-03-11] Challenge #205 [Intermediate] RPN
import re
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


def parser(notation):
    _ = re.split("([)(+-/*])", notation.replace(" ", ""))
    return [part for part in _ if part is not '']

def isnumber(piece):
    return True if piece not in '()\+-*' else False 



print isnumber('*')