def run():
    
    with open('aleph.txt','r', encoding="utf8") as fr:

        with open('aleph2.txt','a') as fw:
            for ln in fr.readlines(): #readlines generates a list with every line
                fw.write(ln)        

def wordCount(vWord):
    counter = 0
    with open('aleph.txt','r',encoding='utf8') as f:
        for ln in f:
            counter += ln.count(vWord)
    
    print('{} se encuentra {} veces en el texto'.format(vWord,counter))

if __name__ == "__main__":
    #run()
    wordCount('Beatriz')