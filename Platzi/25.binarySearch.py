#Efficient way to find some integer value inside an ordered list

import random

numbers = []
numLen = int(input("How many numbers will have your list?: "))
numLow = int(input("Please write the lowest number of the list: "))
numHigh = int(input("please write the bigest number of the list: "))

def fillOrderedList():
    numbers = range(1,numLen+1)

def fillUnorderedList():
    for i in range(0,numLen):

        if i == 0:
            numbers.append(random.randint(numLow,numHigh))
        else:
            while True:
                ranDigit = random.randint(numLow,numHigh)
                if ranDigit not in numbers:
                    numbers.append(ranDigit)
                    break

#        print(numbers)


def binarySearch(numbers,numberToFind,low,high):

    if low > high:
        return False
    
    mid = (low + high) // 2

    if numbers[mid] == numberToFind:
        return True
    elif numbers[mid] > numberToFind:
        return binarySearch(numbers,numberToFind,low,mid-1)
    else:
        return binarySearch(numbers,numberToFind,mid+1,high)

    

if __name__ == "__main__":
    fillUnorderedList()
    numbers.sort()
    #fillOrderedList()
    print()
    numberToFind = int(input("Type an integer number between {} and {} : ".format(numLow,numHigh)))
    print(numbers)
    result = binarySearch(numbers,numberToFind,0,len(numbers)-1)

    if result is True:
        print('number found')
    else:
        print('number not found')