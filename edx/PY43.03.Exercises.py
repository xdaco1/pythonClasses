print("\nExercise 1")
vHours=float(input("Enter Hours: "))
vRate=float(input("Enter Rate: "))
if vHours > 40 :
    vPay = vRate*40 + ((vRate*1.5)*(vHours-40))
print("Pay:",str(vPay))

print('\nExercise 2')
try:
    vHours=float(input("Enter Hours: "))
    vRate=float(input("Enter Rate:"))
    #vPay=vHours*vRate
    #print(vPay)
except:
    print("Error, please enter numeric input")

print('\nExercise 3')
vGrade=""
try:
    vScore=float(input("Enter score: "))

    if vScore < 0 or vScore > 1:
        raise Exception("Bad Score")
    if vScore >= 0.9:
        vGrade="A"
    elif vScore >= 0.8:
        vGrade="B"
    elif vScore >= 0.7:
        vGrade="C"
    elif vScore >= 0.6:
        vGrade="D"
    else:
        vGrade="F"
    
    print(vGrade)

except:
    print("Bad Score")