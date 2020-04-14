import random 

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\\  |
    |   |
   / \\  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def randonword():
    indice = random.choice(WORDS)
    return indice

def main():
    palabra=randonword()
    pales=['-'] * len(palabra)
    error=0
    while True:
        ahorcado(pales, error)
        xd = str(input('ESCOGE UNA LETRA: '))
        nuevo=[]
        for i in range(len(palabra)):
            if xd==palabra[i]:
                nuevo.append(i)
                
        if len(nuevo) == 0:
            error += 1
            if error==7:
                ahorcado(pales,error)
                print('JAJAJAJAJAJAJA PERDISTE')
                print('La palabra correcta era {}'.format(palabra))
                return 
        else:
            for i in range(len(pales)):
                if palabra[i]==xd:
                    pales[i]=xd
        try:
            pales.index('-')
        except ValueError:
            print('GANASTE')
            return 

def ahorcado(palabra, error):
    print(IMAGES[error])
    print('')
    print(palabra)
    print('_*_*_*_*_*_*_*_*_*_*_')

if __name__ == '__main__':
    print("INICIA EL JUEGO")
    main()