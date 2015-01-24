def cannonWords(word):
    word1 = list(word.split()[0])
    word2 = list(word.split()[1])
    for letter1 in word1:
        for letter2 in word2:
            if letter1 == letter2:
                word1.remove(letter1)
                word2.remove(letter2)
    if len(word1) > len(word2):
        return 'First won!' + ' ' + '{0} is bigger than {1}'.format(''.join(word1), ''.join(word2))
    elif len(word1) < len(word2):
        return 'Second won!' + ' ' + '{0} is bigger than {1}'.format(''.join(word2), ''.join(word1))
    else:
        return 'It\'s a tie!'
print cannonWords('amazing amateure')

'''duas palavras

comparar letras

deletar repetidas

juntar'''
