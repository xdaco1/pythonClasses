def palindrome(vWord):
    lWord = list(vWord)
    lWord.reverse()
    rWord = ''.join(lWord)

    if rWord.lower() == vWord.lower():
        print("%s is a palindrome" % (vWord))
    else:
        print("%s is not a palindrome" % (vWord))


if __name__ == "__main__":
    palindrome(input("Write a word: "))
