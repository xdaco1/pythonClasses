import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = ['dishwasher','computer']

def fnRandomWord(maxNum):
    vIndex = random.randint(0,maxNum-1)
    return WORDS[vIndex]


def run():
    vWord = fnRandomWord(len(WORDS))
    vHiddenWord = ['-'] * len(vWord)
    vTries = 0

    while True:
        displayBoard(vHiddenWord,vTries)
        vCurrentLetter = input('Choose a letter: ')

        vLetterIndexes = []

        for i in range(len(vWord)):
            if vWord[i] == vCurrentLetter:
                vLetterIndexes.append(i)

        if len(vLetterIndexes) == 0:
            vTries += 1

            if vTries == len(IMAGES)-1:
                displayBoard(vHiddenWord,vTries)
                print('')
                print("I'm sorry, you lost :( ... The word was {}".format(vWord))
                break

        else:
            for idx in vLetterIndexes:
                vHiddenWord[idx] = vCurrentLetter
            
            vLetterIndexes = []

        try:
            vHiddenWord.index('-')
        except ValueError:
            print('')
            print("Great!! You win!! The word is {}".format(vWord))
            break
        
    
def displayBoard(vHiddenWord, vTries):
    vSeparator = ['* --- * '] * 6
    print(IMAGES[vTries])
    print('')
    print(vHiddenWord)
    print('')
    print(''.join(vSeparator))


if __name__ == "__main__":
    print("**** Welcome to Hangman Game ****")
    run()