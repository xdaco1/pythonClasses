#https://books.trinket.io/pfe/07-files.html#exercises

# Exercise 1
def upperText(vFileName):
    with open(vFileName,'r',encoding='utf8') as f:
        for ln in f.readlines():
            print(ln.upper())

def averageSpamConfidence(vFileName):
    vLines = 0
    sumAverage = 0
    with open(vFileName,'r',encoding='utf8') as f:
        for ln in f.readlines():
            if ln.startswith("X-DSPAM-Confidence:"):
                vLines += 1
                sumAverage += float(ln[ln.index(': ') + 2:])
    print('Average spam confidence: {}'.format((sumAverage / vLines).__round__(12)))

def countSubjectLines(vFileName):
    
    if vFileName == 'na na boo boo':
        print('{} TO YOU - You have been punk\'d!'.format(vFileName.upper()))
    else:

        vLines = 0
        
        try:
            with open(vFileName,'r',encoding='utf8') as f:
                for ln in f.readlines():
                    if ln.lower().startswith('subject'):
                        vLines += 1
                print('There where {} subject lines in {}'.format(vLines,vFileName))
        except FileNotFoundError:
            print('File cannot be opened: missing {} '.format(vFileName))
        

if __name__ == "__main__":
    #upperText('edx/mbox-short.txt')
    #averageSpamConfidence(str(input("Write the name of the file: ")))
    countSubjectLines(str(input(("Write the name of your file: "))))