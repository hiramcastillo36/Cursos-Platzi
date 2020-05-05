from borracho import BorrachoTradicional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio= campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_boracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, intentos, tipodeborracho):
    borracho=tipodeborracho('David')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(intentos):
        campo= Campo()
        campo.add_borracho(borracho, origen)
        simular_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simular_caminata, 1))
    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='pasos recorridos')
    grafica.line(x, y ,legend='distancia')
    show(grafica)

def main(distanciasdecaminatas, intentos, tipodeborracho):
    distanciasmediaxcaminata=[]
    for pasos in distanciasdecaminatas:
        distancias= simular_caminata(pasos, intentos,tipodeborracho)
        distanciamedia=round(sum(distancias) /len(distancias),4)
        distanciamax=max(distancias)
        distanciaminima=min(distancias)
        distanciasmediaxcaminata.append(distanciamedia)
        print(f'{tipodeborracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media = {distanciamedia}')
        print(f'Max = {distanciamax}')
        print(f'Min = {distanciaminima}')
    graficar(distanciasdecaminatas, distanciasmediaxcaminata)

if __name__=="__main__":
    distanciasdecaminatas = [10,100,1000]
    intentos = 100

    main(distanciasdecaminatas, intentos, BorrachoTradicional)
