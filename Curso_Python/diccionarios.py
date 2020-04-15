
def primerdato(diccionario):
    """"for value in diccionario.items(): #values != items
        print(value)"""
    print(diccionario)

def main():
    """diccionario={}
    diccionario['mate'] = 3
    diccionario['lite'] = 5
    diccionario['historia'] = 4
    diccionario['fisica'] = 7
    primerdato(diccionario)"""
    iterate=int(input("Cuantos datos: "))
    datos={}
    for _ in range(iterate):
        nombre=str(input("Materia: "))
        calificacion=int(input("Calificacion: "))
        introducirdatos(datos,  nombre, calificacion)
    primerdato(datos)

def introducirdatos(datos, nombre, calificacion):
    datos[nombre]=calificacion

if __name__=='__main__':
    main()