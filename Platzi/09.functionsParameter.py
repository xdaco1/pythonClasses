# -*- coding: utf-8 -*-

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte Mx a COP')
    print('')

    ammount = float(input("Ingresa la cantidad de pesos mexicanos que quieres convertir: "))

    result = foreignExchangeCalculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('')

def foreignExchangeCalculator(ammount):
    mexToColRate = 145.97

    return mexToColRate * ammount

if __name__ == "__main__":
    run()