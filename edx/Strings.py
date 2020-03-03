vWord="Banana"
x=5
print("letter at",x,"th Position: ",vWord[x])
print("Length of word",vWord,"is",len(vWord))

index=0
while index < len(vWord):
    letter=vWord[index]
    index = index+1
    print(letter)

for vLetter in vWord:
    print(vLetter)

#Slicing Strings
print(vWord[0:4])
print(vWord[5:6])
print(vWord[6:20])
print(vWord[:2])
print(vWord[4:])
print(vWord[:])

#Concatenation
print("Hi " + "World")
print("Hi","World")

#In as logical operator

"n" in vWord
"m" in vWord

if "nan" in vWord:
    print("Found it!!")

#String comparition
if "banana" == vWord.lower(): #This sintax String.function is because the method is part of the String
    print("igual")

print(type(vWord))
dir(vWord)
print(vWord.find("na"))
print(vWord.find("na",3))
print(vWord.upper())
print(vWord.replace("a","o"))

vInputWord = input("Write a word").lower()
if vInputWord == vInputWord[::-1]:
    print("It's a palindrome")
else:
    print("It isn't a palindrome")

for vLetter in vInputWord:
    print(vLetter)

print("hi" + "there")
print("hi","there")

vFruit = input("write the name of a fruit")
print("Searching 'a' in")
if 'a' in vFruit:
    print("yes, it has")
    print("The first 'a' is at",str(vFruit.find('a')+1) + "th position")
    print("But now is",vFruit.replace('a','o'))


# Stripping whitespace
print("  hello bob    ".strip())
print("  hello bob    ".lstrip())
print("  hello bob    ".rstrip())

# Prefixes
print("This is the line".startswith("This"))

# parsing and extracting
vData = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = vData.find("@")
print(atpos)
sppos = vData.find(' ',atpos)
print(sppos)
vHost = vData[atpos+1 : sppos]
print(vHost)

