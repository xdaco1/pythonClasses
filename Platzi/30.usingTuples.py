def firstNotRepeatingChar(charSequence):
    
    for letter in charSequence:
        letterCount = charSequence.count(letter)

        if letterCount == 1:
            return letter
    
    return "_"

if __name__ == "__main__":
    charSequence = tuple(input("Write a sequence of characters separated by comma: "))
    print(type(charSequence))
    result = firstNotRepeatingChar(charSequence)
    if result == '_':
        print("All the characters are repeated")
    else:
        print("The firs character not repeated is: {}".format(result))