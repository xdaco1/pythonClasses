#https://books.trinket.io/pfe/09-dictionaries.html#exercises

#Exercise 2
def mailDayCommit(filename):
    weekDays = dict()

    with open(filename,'r',encoding='utf8') as f:
        for ln in f.readlines():
            if ln.startswith('From '):
                day = ln.split()[2]
                weekDays[day] = weekDays.get(day,0) + 1
    
    print(weekDays)

#Exercises 3 - 4
def getSenderHistogram(logName):
    senderHistogram = dict()

    with open(logName,'r',encoding='utf8') as f:
        for ln in f.readlines():
            if ln.startswith("From "):
                email = ln.split()[1]
                senderHistogram[email] = senderHistogram.get(email,0) + 1

    print(senderHistogram)

    #Getting the mayor sender
    vSender = None
    vQuantity = None
    for sender,quantity in senderHistogram.items():
        if vQuantity is None or vQuantity < quantity:
            vSender = sender
            vQuantity = quantity

    print('The mayor sender is {} with {} emails'.format(vSender,vQuantity))

#Exercise 5
def getDomainHistogram(logname):
    domainHistogram = dict()

    with open(logname,'r',encoding='utf8') as f:
        for ln in f.readlines():
            if ln.startswith("From "):
                domain=ln.split()[1].split('@')[1]
                domainHistogram[domain] = domainHistogram.get(domain,0) + 1
    
    print(domainHistogram)

if __name__ == "__main__":
    #mailDayCommit('mbox-short.txt')
    #getSenderHistogram('mbox-short.txt')
    getDomainHistogram('mbox-short.txt')