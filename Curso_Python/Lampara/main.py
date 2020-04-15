from lamp import Lampara

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