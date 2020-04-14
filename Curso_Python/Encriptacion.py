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

def cifrar():
    palabra=input("Que mensaje quieres cifrar? ")
    palabracifrada=palabra.split(' ') #funcion para separar palabra en espacios
    arreglo=[]
    for x in palabracifrada:
        arreglo2 = ''
        for letra in x:
            arreglo2 += KEYS[letra]
        arreglo.append(arreglo2)
    return ' '.join(arreglo)

def descifrar():
    palabra=input("Que mensaje quieres descifrar? ")
    palabracifrada=palabra.split(' ') #funcion para separar palabra en espacios
    arreglo=[]

    for pal in palabracifrada:
        f=''
        for letra in pal:
            for key, value in KEYS.items():
                if value==letra:
                    f += key
        arreglo.append(f)  

    return ' '.join(arreglo)


def main():
    x = input('''_*_*_*_*_*_*_*_*_*_*_*_*_*_ 
        CRIPTOGRAFIA
        
        Que desea hacer?
            [c]ifrar mensaje
            [d]escrifrar mensaje
            [s]alir
_*_*_*_*_*_*_*_*_*_*_*_*_*_
''')
    if x=='c':
        print(cifrar())
    elif x=='d':
        print(descifrar())
    elif x=='s':    
        return 
    else:
        print("ERROR")
        return 

if __name__ == '__main__':
    print("CIFRAR MENSAJES")
    main()
    