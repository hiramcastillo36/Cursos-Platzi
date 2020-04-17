import csv

class Contacto:
    def __init__(self, name, phone, email):
        self.name=name
        self.phone=phone
        self.email=email

class Agenda:
    def __init__(self):
        self._contactos=[]
    
    def add(self, name, phone, email):
        contacto = Contacto(name, phone, email)
        self._contactos.append(contacto)
        self._guardar()

    def mostrar(self):
        for contacto in self._contactos:
            self._printcontacto(contacto)
    
    def eliminar(self, nombre):
        for idx, contacto in enumerate(self._contactos):
            if contacto.name.lower() == nombre.lower():
                del self._contactos[idx]
                self._guardar()
                break
    
    def buscar(self, nombre):
        for idx, contacto in enumerate(self._contactos):
            if contacto.name.lower() == nombre.lower():
                self._printcontacto(self._contactos[idx]) #Para funciones privadas solo poner self
                break
        else: 
            self._noencontrado()

    def actualizar(self, nombre, phone, email):
        for contacto in enumerate(self._contactos):
            if contacto.name.lower() == nombre.lower():
                contacto.phone=phone
                contacto.email=email

    def _printcontacto(self, contacto):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contacto.name))
        print('Teléfono: {}'.format(contacto.phone))
        print('Email: {}'.format(contacto.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _noencontrado(self):
        print('*********')
        print('NO ENCONTRADO')
        print('*********')

    def _guardar(self):
        with open('contactos.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contacto in self._contactos:
                writer.writerow((contacto.name, contacto.phone, contacto.email))

def main():
    agenda=Agenda()
    try:
        with open('contactos.csv', 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx==0:
                    continue
                agenda.add(row[0],row[1],row[2])
    except FileNotFoundError:
        with open('contactos.csv', 'w', newline='') as f:
            pass


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
            print("A C T U A L I Z A R  C O N T A C T O")
            nombre = input("Dame el nombre: ")
            telefono = input("Dame el telefono del contando: ")
            email = input("Dame el correo: ")
            agenda.actualizar(nombre, telefono, email)
            
        elif command == 'b':
            nombre = input("Dame el nombre para buscar: ")
            agenda.buscar(nombre)

        elif command == 'e':
            nombre = input("Dame el nombre para eliminar: ")
            agenda.eliminar(nombre)

        elif command == 'l':
            agenda.mostrar()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__=='__main__':
    print("B I E N V E N I D O")
    main()