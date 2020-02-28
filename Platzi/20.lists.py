
def average_temps(temps):
    sumOfTemps = 0

    for temp in temps:
        sumOfTemps += temp

    return sumOfTemps / len(temps)

if __name__ == "__main__":
    temps = [21,24,24,22,20,23,24]

    average = average_temps(temps)

    print('La temperatura promedio es: {}'.format(average))