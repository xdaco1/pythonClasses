import sys

def printDict(fileName):
  dict={}
  sortedDict={}

  with open(fileName,'r',encoding='utf8') as f:
    for line in f:
      for key in line.split():
        if key in dict:
          dict[key] +=1
        else:
          dict[key] = 1

  sortedDict=sorted(dict.items(), key=lambda x:x[1], reverse=True)

  for key in sortedDict:
    print(key[0],' ',key[1])
        

if __name__ == "__main__":

    fileName = sys.argv[1]
    print('Processing file: {}'.format(fileName))
    printDict(fileName)