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