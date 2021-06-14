"""
Estructuras de control "WHILE":
"""
#Uso de While infinito:
# c=1
# while True:
#     print(c)
#Uso de While infinito:
c=1
while True:
    print(c)

#While validación 
vocal=input("Ingresa una vocal: ")
while vocal not in ("a","e","i","o","u"):
    if vocal==".":
        break
    vocal=input("vocal: ")
    print("su vocal o punto es: {}".format(vocal))