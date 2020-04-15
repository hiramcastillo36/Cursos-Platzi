
class Contacto:
    def __init__(self, name, phone, email):
        self._name=name
        self._phone=phone
        self._email=email

class Agenda:
    def __init__(self):
        self._contactos=[]
    
    def add(self, name, phone, email):
        print("Name: {}, Phone: {}, Email: {}".format(name,phone, email))


def main():
    agenda=Agenda()
    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            nombre = input("Dame el nombre: ")
            telefono = input("Dame el telefono del contando: ")
            email = input("Dame el correo: ")
            agenda.add(nombre, telefono, email)
        
        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('buscar contacto')

        elif command == 'e':
            print('eliminar contacto')

        elif command == 'l':
            print('listar contactos')

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__=='__main__':
    print("B I E N V E N I D O")
    main()