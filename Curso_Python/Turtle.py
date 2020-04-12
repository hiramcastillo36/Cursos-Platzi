import turtle

window = turtle.Screen()
tortuguin = turtle.Turtle()
x = 150
y = 90 

for i in range(1,15):
    tortuguin.forward(x)
    tortuguin.left(y)
    tortuguin.forward(x)
    tortuguin.left(y)
    tortuguin.forward(x)
    tortuguin.left(y)
    tortuguin.forward(x)
    tortuguin.left(y)
    pos = tortuguin.pos()
    tortuguin.setpos(i*10,i*10)
    x=x-20
    print(pos)
turtle.mainloop()