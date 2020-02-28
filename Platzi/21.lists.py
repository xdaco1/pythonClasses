miLista = []
type(miLista)
miLista.append(1)
miLista2 = [2,3,4]
miLista3 = miLista + miLista2
miLista3
miLista4 = ['a']
miLista5 = miLista4 * 10

utiles = ['lapiz','calculadora','cuaderno']
del utiles[0]
print(utiles)
utiles.remove('cuaderno')
print(utiles)

vCasa='casa'
type(vCasa)
lCasa = list(vCasa)
print(lCasa)
print(''.join(lCasa))