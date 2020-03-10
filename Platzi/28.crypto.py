# for python 3

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cifrar(message):
    words = message.split(' ')
    cypherMessage = []

    for word in words:
        cypherWord = ''
        for letter in word:
            cypherWord += KEYS[letter]

        cypherMessage.append(cypherWord)

    return ' '.join(cypherMessage)

def descifrar(message):
    words = message.split(' ')
    decipherMessage = []

    for word in message:
        decipherWord = ''

        for letter in word:
            for key,value in KEYS.items():
                if value == letter:
                    decipherWord += key

        decipherMessage.append(decipherWord)

    return ' '.join(decipherMessage)


def run():
    while True:
        command = str(input('''Bienvenido a criptografía. ¿Qué deseas hacer?
        
        [c]ifrar mensaje
        [d]escifrar mensaje
        [s]alir
        '''
        ))

        if command == 'c':
            vMessage = str(input("Escribe un mensaje: "))
            cypherMessage = cifrar(vMessage)
            print(cypherMessage)
        elif command == 'd':
            vMessage = str(input("Escribe tu mensaje cifrado: "))
            decypherMessage = descifrar(vMessage)
            print(decypherMessage)
        elif command == 's':
            print('salir')
            break
        else:
            print('¡Comando no encontrado!')

            

if __name__ == "__main__":
    print("M E N S A J E S   C I F R A D O S")
    run()