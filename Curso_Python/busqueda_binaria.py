def busqueda(num, numeros, low, high):
    if low > high:
        return False
    mid=int((low+high)/2)
    if numeros[mid]==num:
        return mid  
    elif numeros[mid]>num:
        print("Clear")
        return busqueda(num, numeros, low, mid-1)
    else:
        print("Clear")
        return busqueda(num,numeros, mid+1, high)

if __name__=='__main__':
    numeros=[1,2,3,4,5,6,7,8,9,10]
    num=int(input("Dame un numero: "))
    resul=busqueda(num, numeros, 0, len(numeros)-1)
    print(resul)