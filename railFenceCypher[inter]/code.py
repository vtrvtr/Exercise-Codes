def railFenceCypher(a):
    l1, l2, l3 = [], [], []
    a = a.upper()
    index = 0
    while index <= len(list(a)) - 1:
        l1.append(a[index])
        l2.append(' ')
        l3.append(' ')
        index += 1
        if index > len(list(a)) - 1:
            break
        else:
            l2.append(a[index])
            l1.append(' ')
            l3.append(' ')
            index += 1
        if index > len(list(a)) - 1:
            break
        else:
            l3.append(a[index])
            l1.append(' ')
            l2.append(' ')
            index += 1
        if index > len(list(a)) - 1:
            break
        else:
            l2.append(a[index])
            l1.append(' ')
            l3.append(' ')
            index += 1
    return '{0}\n{1}\n{2}'.format(''.join(l1), ''.join(l2), ''.join(l3))


def decode(code):
    s = code.split('\n')
    lenOfDecoded = len(code)/3
    decoded = []
    index = 0
    while index < lenOfDecoded:
        for count in range(3):
            if s[count][index] != ' ':
                decoded.append(s[count][index])
        index = index + 1
    return ''.join(decoded)

index = railFenceCypher('thisismyname')
print 'THISISMYNAME'
print index
print decode(index)
