def validator(isbn_number):

    number_List = [int(number)
                   for triple in isbn_number.split('-') for number in triple]
    if len(number_List) == 10:
        n = len(number_List)
        sums = 0
        for number in number_List:
            sums += number * n
            n -= 1
        if sums % 11 == 0:
            return True
    return False


def test():
    print validator('11')


test()
