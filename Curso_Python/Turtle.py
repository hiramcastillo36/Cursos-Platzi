import turtle

def main():
    window = turtle.Screen()
    tortuguin = turtle.Turtle()
    tam=80
    for i in range(1,15):
        dibujar(tortuguin, tam)
        tam = configpos(tortuguin, i, tam)

def dibujar(tortuguin, tam):
    cuadrado(tortuguin, tam)

def configpos(tortuguin, i, tam):
    tortuguin.setpos(i*5,i*5)
    return tam-10

def cuadrado(tortuguin, size):
    for i in range(4):
        tortuguin.forward(size)
        tortuguin.left(90)

if __name__ == '__main__':
    main()