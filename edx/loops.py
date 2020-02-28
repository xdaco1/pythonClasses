vNumber=5
while vNumber >0:
    print(vNumber)
    vNumber=vNumber-1

#Infinite loop using continue and break to control it
while True :
    vWord=input("Write \"ping\", \"pong\" or \"exit\"")
    if vWord=="ping":
        print("marco")
        continue #next iteration
    if vWord=="pong":
        print("polo")
        continue #next iteration
    if vWord=="exit":
        break #exit from loop
print("loop finished")

#for loop
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

friends=["Joseph","Glenn","Sally"]
for friend in friends:
    print("Happy hollydays",friend)
print("Done!")

largest=None
for num in [9,41,12,3,74,15]:
    #"is" operator for logical expressions
    # imples "is the same as"
    # Similar to, but stronger than ==
    # Is not also a logical operator
    # use it for false, true or None.
    if largest is None:
        largest=num
    elif num>largest:
        largest=num
print("largest is:",largest)