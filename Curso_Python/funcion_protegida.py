def proteccion(func):
    def xd(password):
        if password=='Kilinfeo':
            return func()
        else:
            print("INCORRECTA")

    return xd

@proteccion
def funcion_protegida():
    print("Es correcta")


if __name__=='__main__':
    password = input("Password: ")
    funcion_protegida(password)