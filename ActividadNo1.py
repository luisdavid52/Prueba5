# Transcribir los sguientes Pseudocodigos al lenguaje Python
#1Superficie de un circulo
class superficie:
    def __init__(self):
        pass
    def calculo(self):
        r=input("***Ingrese un Numero Real***: ")
        s=r*3.1416
        print("La superficie de un circulo con un Radio de:{}: es igual a:{}".format(r,s))

cal1=superficie()
cal1.calculo()

# 2 En una tienda se ofrece un descuento del 15% sobre el total de la 
# compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.
class ejecicios:
    def __init__(self):
        pass

    def calculo(self):
        tc=input("*Ingrese EL Total de las compras*: ")
        d=tc*0.15
        cp=tc-d
        print("El total de la compra es:{}".format(cp))
        
cal1=ejecicios()
cal1.calculo()

# 3 Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las 
# tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
class comision:
    def __init__(self):
        pass
    
    def calculo(self):
        suelB=input("Por favor mi estimado usuario Ingrese su sueldo base : ")
        v1=input("Ingrese el valor de la venta 1: ")
        v2=input("Ingrese el valor de la venta 2: ")
        v3=input("Ingrese el valor de la venta 3: ")

        TotalV=v1+v2+v3
        com=TotalV+0.1
        TotalR=suelB+com

        print("EL total a recibir sera de:{} dolares".format(TotalR))

cal1=comision()
cal1.calculo()

# 4 cafilicacion de un examen
class calificacion:
    def __init__(self):
        pass

    def calculo(self):
       cal=input("Ingrese su calificacion: ")
       if cal >= 7:
            print("Usted ha Aprovado, felicidades")
      

cal1=calificacion()
cal1.calculo()

# 5 Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación 
# es mayor o igual que 7 y “Reprobado” en caso contrarioCalificacon de un examen con doble salida
class calificacion2:
    def __init__(self):
        pass

    def calculo(self):
       cal=input("Ingrese su calificacion: ")
       if cal >= 7:
            print("Usted ha Aprovado, felicidades")
       else:
            print("Usted Reprobo")
            
cal1=calificacion2()
cal1.calculo()

# 6 Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% 
# si su sueldo es inferior a $600, en caso contrario no tendrá aumento.
# sueldo = input("Ingrese el valor de su sueldo: ")
class sueldo:
    def __init__(self):
        pass

    def calculo(self):
        sueldI=input("Ingrese el sueldo Inicial: ")
        if sueldI < 600:
            sueldN=sueldI+(sueldI*0.10)
        else:
            sueldN=sueldI
            print("su nuevo sueldo es de:{} dolares".format(sueldN))       

cal1=sueldo()
cal1.calculo()

# 7 Determinar la cantidad de dinero que recibirá un trabajador 
# por concepto de las horas extras trabajadas en una empresa, 
# sabiendo que cuando las horas de trabajo exceden de 40, el 
# resto  se consideran horas extras y que éstas se pagan al doble de una hora normal 
# cuando no exceden de 8;  si las horas extras 
# exceden de 8 se pagan las primeras 8 al  doble de lo que se paga por una 
# hora normal y el resto al triple.
class HExtra:
    def __init__(self):
        pass

    def calculo(self):
        ht=input("Ingrese las horas Trabajadas: ")
        ph=input("Ingrese el pago por hora: ")

        if ht > 40:
            he=ht-40
            if he > 8:
                het=he-8
                phe=ph*2*8+ph*3*het
            else:
                phe=ph*2*he

            pt=ph*40+phe
        else:
            pt=ph*ht
            print("EL pago total de horas trabajadas es de:{}".format(pt))

clas1=HExtra()
clas1.calculo()

# 8 Leer los 3 numeros enteros entres si y determinar el mayor de los 3
class Mayor:
    def __init__(self):
        pass

    def calculo(self):
        N1=input("Ingrese el Numero 1: ")
        N2=input("Ingrese el Numero 2: ")
        N3=input("Ingrese el Numero 3: ")

        if (N1 > N2) and (N1 > N3):
            NM=N1
        else:
            if N2 > N3:
                NM=N1
            else:
                NM=N3
        
        print("EL numero mayor es:{}".format(NM))

clas1=Mayor()
clas1.calculo()

# 9 Diseñar un algoritmo tal que dados como datos 
# dos variables de tipo entero, obtenga el resultado de la siguiente función.
class funcion:
    def __init__(self):
        pass

    def calculo(self):
        num=input("Favor Ingresar un numero: ")
        v=input("Ingrese un valor")

        if num == 1:
            resp=100*v
        elif num == 2:
            resp=100**v
        elif num == 3:
            resp=100/v
        else:
            resp=0

        print("El resultado de la funcion seleccionada es:{}".format(resp))

clas1=funcion()
clas1.calculo()
        
# 10 Una escuela aplica dos exámenes a sus aspirantes, 
# por lo que cada uno de ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga 
# calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.
class aspirantes:
    def __init__(self):
        pass
    #usando el operador and 
    def calculo(self):   
        c1=input("Ingrese la primmera calificacion: ")
        c2=input("Ingrese la segunda calificacion: ")
        if c1 >= 80 and c2 >= 80:
            print("aceptado")
        else:
            print("Rechazado")

    #usando el operador or

        if c1>=90 or c2>=90:
            print("aceptado")
        else:
            print("rechazado")

clas1=aspirantes()
clas1.calculo()

# 11 Suma de los cuadrados de los primeros 100 enteros
class sumac:
    def __init__(self):
        pass

    def suma(self):
        sum=0
        for 1 in 100:
            sum=sum+1*1
        print("la suma es{}".format(sum))

clas1=sumac()
clas1.calculo()

# 12 Escribir los numeros del 1 al 100
class numeros:
    def __init__(self):
        pass

    def numeros(self):
        i=1
        while 1 <= 100:
            print(i)
            i=i+1

clas1=numeros()
clas1.calculo()

# 13 Calcular la suma y producto de numeros enteros
class bucle:
    def __init__(self):
        pass

    def calculo():
        suma=0
        prod=1
        resp=input("Ingrese Resp: ")
        while resp == "s"and resp == "n":
            num=("Ingrese un numero: ")
            suma=suma+num
            prod=prod*num
            print("desea continuar(s/n)?")

        print("Total de la suma es:{} ".format(suma))
        print("Total del producto es:{} ".format(prod))

clas1=bucle()
clas1.calculo() 

# 14 Suma y producto de N números enteros, utilizando un bucle controlado por centinela
class enteros:
    def __init__(self):
        pass

    def calculo(self):
        num=input("Ingrese un numero: ")
        while num== -1:
            suma=suma+num
            prod=prod*num
            
        print("El Total de la suma es:{}".format(suma))
        print("EL total del producto es{}".format(prod))

clas1=enteros()
clas1.calculo()

# 15 Determinar si un número entero proporcionado por el usuario es primo

class primo:
    def __init__(self):
        pass

    def calculo(self):
        num=input("Ingrese el numero: ")
        primo=True
        divisor=2
        while ((divisor < num) and (primo == "t")):
            res= num % divisor
            if res==0:
                print("el numero es primo{}".format(primo))
            divisor=divisor+1

        if primo == "t":
            print("el numero:{} es primo".format(num))
        else:
            print("el numero:{} no es primo".format(num))

clas1=primo()
clas1.calculo()

# 16 Leer un número entero N y calcular
class calcular:
    def __init__(self):
        pass

    def calculo(self):
        serie=0
        l=1
        N=input("Ingrese un Numero: ")
        band="T"
        while True:
            if band == "T":
                Serie=serie + (1/l)
                band="F"
            else:
                Serie=serie-(1/l)
                band="T"
            l=l+1
            if l > N:
                print(serie)

clas1=calcular()
clas1.calculo()

# 17 Calcular el factorial de N números enteros leídos de teclado.
# El problema consistirá en realizar una estructura de N 
# iteraciones aplicando el factorial de un número.
class factorial:
    def __init__(self):
        pass

    def calculo(self):
        N=input("Ingrese la cantodad de numeros: ")
        for i in N:
            numero=input("Ingrese el numero: ")
            fact=1
            for j in numero:
                fact=fact*j
            print("EL factorial del numero:{} es:{}".format(numero,fact))

clas1=factorial()
clas1.calculo()

# 18 Aplicar las fases  para  la resolución de un problema para leer un vector de 20 
# números enteros y a continuación escribir en un vector A todos los números negativos y 
# en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.
class vector:
    def __init__(self):
        pass

    def calculo(self):
        j=1
        k=1
        num=20
        A=20
        B=20
        for i in 20:
            num=i
            if num>0:
                j=num
                j=j+1
            else:
                k=num
                k=k+1
            
            for i in j:
                print(A)
            
            for i in k:
                print(B)
            
clas1=vector()
clas1.calculo()


# 19 Se tiene información sobre las calificaciones de 6 
# exámenes de un grupo de 30 alumnos. Los datos sobre estos exámenes 
# se proporcionan de la siguiente manera:
# Donde Cali,j es una variable real que expresa la calificación que obtuvo el alumno i en el examen j. 
# Calcular lo siguiente:
# a) el promedio de calificaciones de cada uno de los 6 exámenes
# b) el promedio de cada alumno
# c) el tipo (número) de examen que tuvo el mayor promedio de calificación. Escriba también dicho promedio.
class infCal:
    def __init__(self):
        pass

    def calculo(self):
        for i in 30:
            for j in 6:
                print("Escriba la calificacion del alumno:{} en el examen{}".format(i,j))
                print(i,j)

        for j in 6:
            sum=0
            for i in 30:
                sum=sum+(i,j)
            prom=sum/30
            print("EL promedio del examane",j,prom)

        for i in 30:
            sum=0
            for j in 6:
                sum=sum+(i,j)

            print("El promedio del alumno es: ", i, sum/6)

        Examen=1
        promayor=prom
        for j in 6:
            if promayor<j:
                promayor=j
                Examen=j
        
        print("El examen:{} obtuvo el mayor promedio:{}".format(Examen,promayor))

clas1=infCal()
clas1.calculo()