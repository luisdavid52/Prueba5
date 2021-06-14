"""
Ciclos
"""
class Ciclos:
    def __init__(self,num1=5):
       self.numero=num1
       
    def usoWhile(self):
        car=input("Ingrese una vocal-> ")
        car=car.lower()
        while car not in ("a","e","i","o","u"):
            car=input("Error, debe ingresar una vocal: ")
        print("Felicidades, el caracter:{} es una vocal".format(car))
     
ciclo1=Ciclos()
ciclo1.usoWhile()
       