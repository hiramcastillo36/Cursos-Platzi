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