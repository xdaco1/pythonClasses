#https://books.trinket.io/pfe/04-functions.html#exercises

print("\nExercise 6")

def computepay(hours,rate):

    vPay=float(0)

    if hours > 40:
        vPay=40*rate
        vPay=vPay+((hours-40)*(rate*1.5))
    else:
        vPay=hours*rate

    return vPay

vHours=float(input("Enter Hours: "))
vRate=float(input("Enter Rate: "))

print(computepay(vHours,vRate))

####

print('\nExercise 7')
def computegrade(score):
    vGrade=""
    try:

        score=float(score)

        if score < 0 or score > 1:
            raise Exception("Bad Score")
        if score >= 0.9:
            vGrade="A"
        elif score >= 0.8:
            vGrade="B"
        elif score >= 0.7:
            vGrade="C"
        elif score >= 0.6:
            vGrade="D"
        else:
            vGrade="F"
        
        return vGrade

    except:
        return "Bad Score"

vScore=input("Enter score: ")
computegrade(vScore)