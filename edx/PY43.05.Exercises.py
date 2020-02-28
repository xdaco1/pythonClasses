#https://books.trinket.io/pfe/05-iterations.html#exercises
#Exercise 1

iData=""
vTotal=0
vCount=0
vAvg=0
while True:
    iData=input("Enter a number: ")

    if iData == "done":
        break
    else:
        try:
            vTotal=vTotal+int(iData)
            vCount=vCount+1
        except :
            print("Invalid input")
            continue
vAvg=vTotal/vCount
print(vTotal,vCount,vAvg)

#Exercise 2
iData=""
minVal=None
maxVal=None
while True:
    
    iData=input("Enter a number")

    if iData=="done":
        break
    else:
        try:
            if minVal is None or maxVal is None:
                minVal=float(iData)
                maxVal=float(iData)
            else:
                if minVal > float(iData):
                    minVal=float(iData)
                if maxVal < float(iData):
                    maxVal=float(iData)

        except :
            print("Invalid input")
            continue

print("Minvalue:",minVal)
print("Maxvalue:",maxVal)