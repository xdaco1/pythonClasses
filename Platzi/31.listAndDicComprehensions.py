# Creation and initializations of lists and dictionaries with a syntax more natural
# Cast of sequences

even = []
for num in range(1,31):
    if num % 2 == 0:
        even.append(num)

print(even)

#With list comprehension

even.remove

even = [num for num in range(1,31) if num % 2 == 0]

print(even)

sqr = {}

for num in range(1,11):
    sqr[num] = num ** 2

print(sqr)

#Using dictionary comprehension
sqr.clear

sqr = {num: num ** 2 for num in range(1,11)}
print(sqr)
