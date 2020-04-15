def busqueda(cadena):
    diccionario = {}
    for first in cadena:
        contador=0
        for second in range(len(cadena)):
            if first==cadena[second]:
                contador=contador+1
        introducirdatos(diccionario, first, contador)
    dato=verificar(diccionario)
    if dato!= '_':
        print("Primer letras es: {}".format(dato))
    else:
        print("Todas se repiten")

def verificar(diccionario):
    for key, value in diccionario.items():
        if value==1:
            return key
    return '_'

def imprimirdatos(diccionario):
    for value in diccionario.items(): #values != items
        print(value)

def introducirdatos(datos, nombre, calificacion):
    datos[nombre]=calificacion

def main():
    cadena=input("Dame un string: ")
    busqueda(cadena)

if __name__ == '__main__':
    main()