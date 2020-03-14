#https://books.trinket.io/pfe/10-tuples.html#exercises

#Exercise 1
def createDict(filename):
    myDict = dict()
    with open(filename,'r',encoding='utf8') as f:
        for ln in f.readlines():
            if ln.startswith("From "):
                vEmail = ln.split()[1]
                myDict[vEmail] = myDict.get(vEmail,0) + 1

    topEmail = sorted( [ (v,k) for k,v in myDict.items() ], reverse=True )[0]

    print('Top email is {} with {} ocurrences.'.format(topEmail[1],topEmail[0]))

#Exercise 2
def getHourDistribution(filename):
    hourDict = dict()
    with open(filename,'r',encoding='utf8') as f:
        for ln in f.readlines():
            if ln.startswith("From "):
                vHour = ln.split()[5].split(':')[0]
                hourDict[vHour] = hourDict.get(vHour,0) + 1
    
    #for k,v in sorted(hourDict.items()):
    #    print(k,v)

    #Using tuples

    hourCatalog = [ (k,v) for k,v in hourDict.items()]
    print(hourCatalog)
    for key,value in sorted(hourCatalog):
        print(key,value)

#Exercise 3
#https://en.wikipedia.org/wiki/Letter_frequency

def letterCount(filename):
    letterDict = dict()
    with open(filename,'r',encoding='utf8') as f:
        for ln in f.readlines():
            for letter in ln.lower():
                if letter.isalpha():
                    letterDict[letter] = letterDict.get(letter,0) + 1
    

    #for k,v in sorted(letterDict.items()):
    #    print(k,v)

    letterCatalog = sorted([ (v,k) for k,v in letterDict.items()], reverse = True)
    for k,v in letterCatalog:
        print(v,k)
    

if __name__ == "__main__":
    #createDict('mbox.txt')
    #getHourDistribution('mbox-short.txt')
    letterCount('mbox-short.txt')