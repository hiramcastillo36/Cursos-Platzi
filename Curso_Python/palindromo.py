
def palindromo(palabra):
    for i in range(len(palabra)):
        if palabra[i] != palabra[len(palabra)-i-1]:
            return 0
    return 1

if __name__ == '__main__':
    palabra = input("Dame una palabra: ")
    print(palindromo(palabra))
