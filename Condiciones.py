"""
Condiciones
"""
class Condicion:
    contador = 0
    def __init__(self,num1=0,num2=1):
        self.numero1=num1 #Variables de intancias
        self.numero2=num2
        # numero=num1+num2
        self.numero3=num1
    def usoIf(self):
        if self.numero1 == self.numero2:
            print("NUMERO1:{}, NUMERO2{}: SON IGUALES".format(self.numero1,self.numero2))
        elif self.numero1== self.numero2:
            print("numero1:{},numero3:{}: son iguales".format(self.numero1,self.numero3))
        else:
            print("No son iguales.")
            
#Uso de clases            
# cond1=Condicion()
# print(cond1.numero1)
# print(cond1.numero2) 
# cond2=Condicion(30)
# print(cond2.numero1)
# print(cond2.numero2)
cond2=Condicion(10,20)
cond2.usoIf()
print(cond2.numero1)