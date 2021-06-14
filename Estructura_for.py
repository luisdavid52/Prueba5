"""
Estructuras de control -"FOR":
"""
#For range(v)- RANGE(VI,VF)-range(vi,vf,inc)
frase=input("Ingrese frase:")
for indice in range((len(frase))):
    print(indice,"=",frase[indice])
#for in cadena - in(tupla)-in[lista]
""" cvoc=0
for car in frase:
    if car in("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print("cantidad vocales:{}".format(cvoc))
#COMPREHENSION - [VAR FOR VAR IN DATOS CONDICION]
[car for car in["a","e","i","o","u"]if in car not in ("a","i","o")] """