import random

def tirardado(numerodetiros):
    secuenciadetiros = []
    for _ in range(numerodetiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuenciadetiros.append(tiro)
    

    return secuenciadetiros

def main(numerodetiros, intentosimu):
    tiros = []
    for _ in range(intentosimu):
        secuenciasdtiros = tirardado(numerodetiros)
        tiros.append(secuenciasdtiros)
    tiros1=0
    for tiro in tiros:
        if 1 in tiro:
            tiros1+=1
    
    probabilidad = tiros1 / intentosimu
    print(f"La probabilidad de 1 es: {probabilidad}")

if __name__=='__main__':
    numerosdetiros=int(input("Cuantos tiros prro? "))
    intentosimu=int(input("Cuantas veces correra la simulacion: "))
    main(numerosdetiros, intentosimu)