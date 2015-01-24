def negativeMod(number, base):
    mod = number
    while number <= 0:
        number += base
    return number


def baseConversion(number, base):
    converted = []
    #test = number - (number // base * base) 
    while number >= 1:
        number, quot = divmod(number, base)
        converted.insert(0,quot)
    return ''.join(str(x) for x in converted)






print baseConversion(100312311242, 20)
# print negativeMod(-10, -3)
''' 357
178 1
89 0
44 1
22 0
11 0
5 1
2 1
1 0

101100101

200
100 0
50 0
25 0
12 1 
6 0
3 0
2 1
1 


11001000
11001000'''


