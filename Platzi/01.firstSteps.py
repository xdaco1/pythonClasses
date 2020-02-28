# -*- coding:utf-8 -*-

# Functions
def helloWorld(name):
    who=input("What's your name?")
    return "Hello " + name + "!!"

print(helloWorld("Vincent"))

#Lists
vList=["me","you",1,2]
print(vList[0])
vList[0]="not me"
print(vList[0])

#Tuples
vTuple=("me","you",1,2)
print(vTuple)
try:
    vTuple[0]="not me"
    print(vTuple)
except :
    print("is not possible to edit a tuple")

#Dictionaries
vDict={
    "Kill bill": "Tarantino",
    "Amelie": "Jean-Pierre Jeunet"
}
print(vDict)
print(vDict["Amelie"])

#Data Casting
print(int(4.3))
print(float(4.0))
print(type(str(4.3)))
print(list((4,5,2)))

#Common operators
## Casting to a set as a list
map(str,[1,2,3,4])

## Get a range
print(range(5))

## Sum a set
print(sum([1,2,3]))

## Sort a set
print(sorted([5,2,8,4]))

## Know commands over a data type
dir(vList)

## Info about a library
help(sorted)


#Classes
class Student(object):
    def __init__(self,name,age):
        self.vName = name
        self.vAge = age

    def sayHi(self):
        return "My name is %s and I'm %i" % (self.vName, self.vAge) 
        #%s for string and %i for integer

vStudent = Student("Daniel",35)
print(vStudent.sayHi())

#Special Methods
#cmp(self,other) #Object comparision
