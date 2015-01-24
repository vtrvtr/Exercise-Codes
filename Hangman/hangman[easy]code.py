import random


def LoadList(wordlist):
	with open(wordlist) as f:
		listOfWords = f.read().splitlines()
		listOfWords.sort(key=len)
	return listOfWords

def Spacing(word):
	spacedWord = []
	for char in word:
		if char.isalpha():
			spacedWord.append("_")
		else:
			pass
	return spacedWord
			


def playHangman(wordlist, numberOfLetters = 5):
	if numberOfLetters < 5:
		raise Exception("Choose more letters!")
	listOfWords = LoadList(wordlist)
	filteredList = filter(lambda word: len(word) < numberOfLetters, listOfWords)
	randomWord = random.choice(filteredList)
	spacedWord = Spacing(randomWord)
	currentWord = spacedWord
	lives = len(spacedWord)
	guessedLetters = []
	while lives > 0:
		guess = raw_input('Guess one letter! ')
		if guess == "":
			print "That's not a letter! Try again! And..."
			break
		else:
			if guess[0] in randomWord:
				for index, char in enumerate(randomWord):
					if char == guess[0]:
						currentWord[index] = randomWord[index]
						
			else:
				lives -= 1
		guessedLetters.append(guess[0])
		print 'Remaining lives', lives
		print 'Guessed Letters:', guessedLetters
		print ''.join(currentWord)
		if currentWord == list(randomWord):
			print "You won!"
			break
	print "You lost! The word was", ''.join(randomWord)






def tests():
	listpath = "E:\code\hangman-wordlist.txt"
	# test1 = LoadList("E:\code\hangman-wordlist.txt")
	# print test1
	# test2 = Spacing("lol's")
	# print test2
	playHangman(listpath, 12)
	

tests()
