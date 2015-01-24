class RomanNumbers(object):

    def __init__(self, number):
        self.number = number

    def toNormal(self):
        numbers = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL':
                   40, 'L': 50, 'XC': '90', 'C': 100, 'D': 500, 'XD': 400, 'CM': 900, 'M': 1000}
        for key, value in numbers.items():
            if key == self.number:
                return numbers[key]

    def toRoman(self):
        numbers = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40:
                   'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        for key, value in numbers.items():
            if key == self.number:
                return numbers[key]

    def __str__(self):
        return self.number


def DecomposeNumber(numbers):

    bigNumberList = []
    for item in numbers:
        numbersList = []
        if item > 4000:
            pass
        else:
            while (item - 1000 >= 0):
                numbersList.append(1000)
                item -= 1000
            while (item - 900 >= 0):
                numbersList.append(900)
                item -= 900
            while (item - 500 >= 0):
                numbersList.append(500)
                item -= 500
            while (item - 400 >= 0):
                numbersList.append(400)
                item -= 400
            while (item - 100 >= 0):
                numbersList.append(100)
                item -= 100
            while (item - 90 >= 0):
                numbersList.append(90)
                item -= 90
            while (item - 50 >= 0):
                numbersList.append(50)
                item -= 50
            while (item - 40 >= 0):
                numbersList.append(40)
                item -= 40
            while (item - 10 >= 0):
                numbersList.append(10)
                item -= 10
            while (item - 9 >= 0):
                numbersList.append(9)
                item -= 9
            while (item - 5 >= 0):
                numbersList.append(5)
                item -= 5
            while (item - 4 >= 0):
                numbersList.append(4)
                item -= 4
            while (item - 1 >= 0):
                numbersList.append(1)
                item -= 1
        bigNumberList.append(numbersList)
    return bigNumberList


def convertToRoman(numbers):
    
    listOfLists = []
    for numbersList in numbers:
    	convertedList = []
        for number in numbersList:
            sign = RomanNumbers(number).toRoman()
            convertedList.append(sign)
	listOfLists.append(convertedList)
    return listOfLists


def test():

    # print a.toRoman()
    a = DecomposeNumber([1345, 2, 452, 42, 3234, 2341, 1113, 231, 111])
    print a
    # for item in convertToRoman(a):
    # 	print ''.join(item)
    a = 3543
    b = str(a)
    c = map(lambda d: 10 ** d, range(len(b))[::-1])

    for n in zip(map(int, b), c):
        print n
test()
