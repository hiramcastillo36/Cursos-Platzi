
def calcular(monto):
    divisa=150.56
    return divisa*monto

def main():
    print("C A L C U L A D O R A  D E  D I V I S A S")
    print("Pesos mexas a pesos colombianos")
    monto = float(input("Cantidad: ")) 
    pesoscolombianos=calcular(monto)
    print('${} pesos mexicanos son ${} pesos colombianos'.format(monto, pesoscolombianos))

if __name__ == '__main__':
    main()