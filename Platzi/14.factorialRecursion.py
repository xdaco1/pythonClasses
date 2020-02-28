#Recursión (es una técnica): Una función puede llamarse a sí misma
#adentro de ella.


def factorial(vNumber):
    if vNumber == 0: #Caso Base
        return 1

    return vNumber * factorial(vNumber -1)


if __name__ == "__main__":
    vNumber = input("Escribe un número: ")
    print(factorial(int(vNumber)))

vString="myString"
print(len(vString))