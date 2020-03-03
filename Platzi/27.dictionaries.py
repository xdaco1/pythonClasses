dict1 = {}
dict2 = dict()
dict2['firstValue'] = 'Hi'
dict2['secondValue'] = 'There'
print(dict2['firstValue'])

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['matemáticas'] = 10
calificaciones['web'] = 8
calificaciones['basesDeDatos'] = 10

print(calificaciones)

for key in calificaciones:
    print(key)
    print(calificaciones[key])

for value in calificaciones.values():
    print(value)

for key,value in calificaciones.items():
    print('key: {}, value: {}'.format(key,value))

sumNote = 0
for note in calificaciones.values():
    sumNote += note

average = sumNote/len(calificaciones)
print("Average: {}".format(average))