class Lampara: #Normalmente con mayuscula
    _lamparas=['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
    def __init__(self, estado): #Constructor (instancia de la clase)
        self.estado=False

    def encender(self): #publico
        self.estado=True
        self._mostrar()

    def apagar(self): #publico
        self.estado=False
        self._mostrar()

    def _mostrar(self): #privado
        if self.estado:
            print(self._lamparas[0])
        else:
            print(self._lamparas[1])


def run():
    lamp = Lampara(estado=False)
    while True:
        x = input('''_*_*_*_*_*_*_*_*_*_*_*_*_*_ 
        CRIPTOGRAFIA
        
        Que desea hacer?
            [e]ncender
            [a]pagar
            [s]alir
_*_*_*_*_*_*_*_*_*_*_*_*_*_
''')
        if x=='e':
            lamp.encender()
        elif x=='a':
            lamp.apagar()
        elif x=='s':    
            return 
        else:
            print("ERROR")
            return 

if __name__=='__main__':
    run()