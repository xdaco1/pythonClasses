# -*- coding: utf-8 -*-

def sumRecursion(num):

    if num == 1: 
        return 1

    return num + sumRecursion(num - 1)

if __name__ == "__main__":
    print(sumRecursion(int(input('Escribe un numero: '))))