def countLines():
    fhand = open('aleph.txt',encoding='utf8')
    vCountLines = 0
    for ln in fhand:
        vCountLines += 1
    fhand.close()
    print("Total of lines: {}".format(vCountLines))

def countCharacters():
    fhand = open('aleph.txt',encoding='utf8')
    inp = fhand.read()
    print('Total of characters: {}'.format(len(inp)))

def printFirstNCharacters(vCharsQty):
    fhand = open('aleph.txt',encoding='utf8')
    inp = fhand.read()
    print('first {} characters: {}'.format(vCharsQty, inp[:vCharsQty]))

def findLineOfText(vTextToSearch):
    vLinesOfText = []
    vLine = 0
    with open('aleph.txt','r',encoding='utf8') as f:
        for ln in f.readlines():
            vLine += 1
            if vTextToSearch in ln:
                vLinesOfText.append(vLine)
        print('"{}" word is present in lines {}'.format(vTextToSearch,vLinesOfText))

if __name__ == "__main__":
    countLines()
    countCharacters()
    printFirstNCharacters(20)
    findLineOfText('Beatriz')