def main(number):
    l = [[] for _ in range(3)]
    number = [int(n)
              for n in str(number).strip()]
    number_dict = {
        0: [' _ ', '| |', '|_|'],
        1: ['   ', ' | ', ' | '],
        2: [' _ ', ' _|', '|_ '],
        3: [' _ ', ' _|', ' _|'],
        4: ['   ', '|_|', '  |'],
        5: [' _ ', '|_ ', ' _|'],
        6: [' _ ', '|_ ', '|_|'],
        7: [' _ ', '  |', '  |'],
        8: [' _ ', '|_|', '|_|'],
        9: [' _ ', '|_|', '  |']
    }
    for n in number:
        for k, v in number_dict.iteritems():
            if k == n:
                for index, value in enumerate(v):
                    l[index].append(value)
    for item in l:
        print ''.join(item)

if __name__ == "__main__":
    while True:
        inpt = raw_input("Number to convert \n")
        try:
            if inpt == 'exit':
                break
            else:
                main(inpt)
        except ValueError:
            'Only numbers please'
