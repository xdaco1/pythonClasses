# Get the name of the file and open it
fileName=input('Enter file name: ')
handle=open(fileName,'r')

# Count word frequency
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

# Find the most common word
bigCount= None
bigWord=None
for word,count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord=word
        bigCount=count

# All done
print(bigWord,bigCount)