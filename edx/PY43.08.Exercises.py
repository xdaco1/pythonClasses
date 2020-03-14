#https://books.trinket.io/pfe/08-lists.html#exercises

#Exercise 1
def chop(listParam):
    listParam.remove(listParam[0])
    listParam.remove(listParam[len(listParam)-1])
    print(listParam)
    return None

#Exercise 4
def readRomeo():
    wordList = []
    with open('romeo.txt','r',encoding='utf8') as f:
        for ln in f.readlines():
            tempWordList = ln.split()
            for vWord in tempWordList:
                if len(vWord) == 0 or vWord not in wordList:
                    wordList.append(vWord)
    wordList.sort()
    print(wordList)

#Exercise 5
def getInbox(fileName):
    inboxList = []
    with open(fileName,'r',encoding='utf8') as f:
        for ln in f.readlines():
            if ln.startswith('From'):
                vMailBox = ln.split()
                inboxList.append(vMailBox[1])

    for item in inboxList:
        print(item)

    print('There were {} lines in the file whith From as the first word'.format(len(inboxList)))

#Exercise 6
def maxAndMin():
    numbersList = []

    while True:
        inp = input("Enter a number: ")

        if inp.isdigit():
            numbersList.append(int(inp))
            
        elif inp == 'done':
            break

    print('Maximum: {}'.format(float(max(numbersList))))
    print('Minimum: {}'.format(float(min(numbersList))))


if __name__ == "__main__":
    #print(chop([1,2,3,4,5]))
    #readRomeo()
    #getInbox(str(input("Enter a file name: ")))
    maxAndMin()
