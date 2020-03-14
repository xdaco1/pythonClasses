def firstCountTest():
    counts = dict()
    names = ['csev','cwen','cwen','zqian','csev']
    for name in names:
        counts[name] = counts.get(name,0) + 1
    print(counts)

def createDictFromFile(fileName):
    myDict = dict()

    with open(fileName,'r',encoding='utf8') as f:
        for ln in f.readlines():
            for word in ln.split():
                myDict[word] = myDict.get(word,0) + 1

    #Getting the most common word
    bigWord = None
    bigCount = None
    for k,v in myDict.items():
        if bigCount is None or v > bigCount:
            bigWord = k
            bigCount = v
    
    print('The most common word in {} is "{}" with {} ocurrences.'.format(fileName,bigWord,bigCount))


if __name__ == "__main__":
    createDictFromFile('../aleph.txt')