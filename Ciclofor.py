class For:
    def __init__(self):
        pass
    def usoFor(self):
        datos=["Daniel",50,True]
        numeros=(2,5.6,4,1)
        docente={"Nombre": "Daniel","Edad":50,"Fac":"Faci"}
        listaNotas=[(30,40),[20,40],(50,40)]
        listaAlumnos=[{"Nombre":"Erick","final":70},{"Nombre" : "Yady", "final" :80},{"Nombre" : "Dani", "final" :90}]
        for i in range(5):
            print("i= {}".format(i))
        for i in range(2,10):
            print("i= {}".format(i))
        for i in range(4,10,2):
            print("i= {}".format(i),end=" ")
        for i in range(12,3,-3):
            print("i= {}".format(i),end=" ")
        longitud= len(datos)
        print(datos[0])
        print(datos[1])
        print(datos[2])
        j=0
        while j<longitud:
            print("While",datos[j])
            j+=1
        for i in range(longitud-1,-1,-1):
            print("for",datos[i])
        for i in range(longitud):
            print(datos[i])
        for i,dato in enumerate(datos):
            print("for",i,dato)
        for dato in numeros:
            print(dato)
        for dato in ["h","o","l","a","que","tal"]:
            print(dato)
        print("\nDiccionario de notas")
        for clave,valor in docente.items():
            print(clave,":",valor,end=" ")
        for alumnos in listaAlumnos:
            for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
bucle1= For()
bucle1.usoFor()
        


listaNotas = [(30,40),[20,40,20],(50,40,20,10)]
acum=0
long=0
for notas in listaNotas:
    parcial=0
    print(notas,end=" ")
    for nota in notas:
        print(nota)
        long+=1
        acum+=nota
        parcial+=nota
    promedioParcial=parcial/len(notas) 
    print("Notas parciales= {}\nPromedio parcial= {}\n".format(parcial,promedioParcial))
prom=acum/long
print("Total notas= {} - #Notas = {} : Promedio= {}".format(acum,long,prom))


listaAlumnos=[{"Nombre":"Erick","final":70},{"Nombre" : "Yady", "final" :80},{"Nombre" : "Dani", "final" :90}]
acum=0
cont=0
for alumnos in listaAlumnos:
    print(alumnos)
    for clave,valor in alumnos.items():
        print(clave,":",valor,end=" ")
        if clave=="final":acum+=valor
    cont+=1
print(acum/cont)


frase= "Hola cómo estás"
vocales=[]
for car in frase:
    if car in ("a","e","i","o","u"):
        vocales.append(car)
print(vocales) 

frase= "Hola cómo estás"
vocales=[car for car in frase if car in("a","e","i","o","u")]
print(vocales)
