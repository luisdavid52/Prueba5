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