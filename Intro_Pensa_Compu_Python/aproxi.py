def main(num):
    epsilon=0.1
    paso=epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - num) >= epsilon and respuesta <= num:
        print(abs(respuesta**2-num), respuesta)
        respuesta += paso

    if abs(respuesta**2-num) >= epsilon:
        print(f"No se encontro raiz {respuesta}")
    else:
        print(f"La raiz es {respuesta}")
if __name__=='__main__':
    num=int(input("Dame un numero: "))
    main(num)