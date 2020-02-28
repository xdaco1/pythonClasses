import turtle

def main():
    window = turtle.Screen()
    t = turtle.Turtle()

    makeSquare(t)

    turtle.mainloop()

def makeSquare(t):
    length = int(input("Tamaño del cuadrado: "))

    for i in range(4):
        makeLineAndTurn(t,length)

def makeLineAndTurn(t,length):
    t.forward(length)
    t.left(90)

if __name__ == "__main__":
    main()