"""
Variables de python
"""
#Numéricos
edad,_peso=50,70.5

#Strig
nombres="Daniel Vera"
dirDomiciliaria="Chile y Guayaquil"
Tipo_sexo="M"

#Boolean
Civil=True

#Colecciones
usuario=('dchiki','1234','chiki@gmail.com')
materias=["Programación web","php","poo"]
docente={"nombre":"daniel","edad":50,"fac":"faci"}

#Imprimir
print("""Mi nombre es {}, tengo {} años""".format(nombres, edad))
print(usuario,materias,docente)

"""
Estructuras de control 
"""
x=int(input("Ingresa un número entero: "))
if x<0:
    x=0
    print("negativo cambiado a cero")
elif x==1:
    print("uno")
else:
    print("Ninguna opción")
print("Ok")if type(x)== int else print("-")

"""
Estructuras de control "WHILE":
"""
#Uso de While infinito:
# c=1
# while True:
#     print(c)

#While validación 
vocal=input("Ingresa una vocal: ")
while vocal not in ("a","e","i","o","u"):
    if vocal==".":
        break
    vocal=input("vocal: ")
    print("su vocal o punto es: {}".format(vocal))
    
"""
Estructuras de control -"FOR":
"""
#For range(v)- RANGE(VI,VF)-range(vi,vf,inc)
frase=input("Ingrese frase:")
for indice in range((len(frase))):
    print(indice,"=",frase[indice])
#for in cadena - in(tupla)-in[lista]
cvoc=0
for car in frase:
    if car in("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print("cantidad vocales:{}".format(cvoc))
#COMPREHENSION - [VAR FOR VAR IN DATOS CONDICION]
[car for car in["a","e","i","o","u"]if in car not in ("a","i","o")]

"""
Funciones en python - "DEF":
"""
#Funciones sin retorno
def vocales(frase):
    for car in frase:
        if car in ("a","e","i","o","u"):
            print(car)
            
#Llamada a función
oracion=input("Ingrese una oración: ")
vocales(oracion.lower())

#Función con retorno de valor
def promedio(notas):
    summ=0
    for n in notas:
        summ+=n
        return summ/len(notas)

#LLamada a la función
listanotas=[2,4,6,8,10]
prom=promedio(listanotas)
print("Promedio:{}={}".format(listanotas, prom))     

"""
Funciones en python-"PREDEFINIDAS":
"""
#Funciones matematicas
import math
mensaje="Hola"+"mundo"+"Python"
men1=mensaje.split()
men2="".join(men1)
print(mensaje[0]) 

#Funciones cadenas
mensaje= "Hola" + "mundo" + "Python"
men1=mensaje.split()
men2="".join(men1)
print(mensaje[0],mensaje[0:4],men1,men2)
print(mensaje.find("mundo"),mensaje.lower())

#Funciones fecha
from datetime import datetime, timedelta, date
hoy,fdia=datetime.now(),date.today()
futuro=hoy+timedelta(days=30)
dif,aa,mm,dd=futuro-hoy,hoy.year,hoy.month,hoy.day
fecha=date(aa,mm,dd+2)
print(hoy,fdia,futuro,dif,fecha)





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
       