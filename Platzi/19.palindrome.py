import random
def main():
    pWord = palindrome(vWord)

    if pWord.lower() == vWord.lower():
        print("It's a palindrome")
    else:
        print("It isn't a palindrome")

def palindrome(vWord):
    return vWord[::-1]


if __name__ == "__main__":
    vWord = input("Write a word: ")
    main()