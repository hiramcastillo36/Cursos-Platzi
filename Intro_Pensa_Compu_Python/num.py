
def main(num):
    res=0
    while res**2 < num:
        print(res)
        res+=1

    if res**2 == num:
        print(f"Raiz es {res}") 
    else:   
        print("No tiene raiz exacta")
if __name__=='__main__':
    num=int(input("Dame un numero: "))
    main(num)