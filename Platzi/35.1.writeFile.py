#write a file
def run():
    #"with" clause is context manager so it's not necessary to close
    with open('numbers.txt','w') as f:
        for i in range(10):
            f.write(str(i)+'\n')

if __name__ == "__main__":
    run()