
def primerdato(diccionario):
    for value in diccionario.items(): #values != items
        print(value)

def main():
    diccionario={}
    diccionario['mate'] = 3
    diccionario['lite'] = 5
    diccionario['historia'] = 4
    diccionario['fisica'] = 7
    primerdato(diccionario)


if __name__=='__main__':
    main()