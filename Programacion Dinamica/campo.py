class Campo:
    def __init__(self):
        self.coordenadas_de_borrachos={}

    def add_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_boracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordena_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordena = coordena_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordena

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]
