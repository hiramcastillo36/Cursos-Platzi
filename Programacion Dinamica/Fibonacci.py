def fib(n):
    if n==0 or n==1:
        return 1
    
    return fib(n-1) + fib(n-2)

def fib_dina(n, mem= {}):
    if n==0 or n==1:
        return 1
    
    try:
        return mem[n]
    except KeyError:
        resultado = fib_dina(n-1) + fib_dina(n-2)
        mem[n]= resultado
    
        return resultado

if __name__=="__main__":
    n = int(input("Dame un numero: "))
    resultado = fib_dina(n)
    print(resultado)