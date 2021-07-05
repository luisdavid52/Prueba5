#class Operaciones
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2

    def suma(self):
        sum = self.numero1 + self.numero2
        return sum

    def resta(self):
        if self.numero1 >= self.numero2:
            return self.numero1 - self.numero2
        return 0
    def multiplicacion(self):
        return self.numero1 * self.numero2

    def division(self):
        if self.numero2  !=0:
            return self.numero1 / self.numero2
        return 0
    def division_entera(self):
        return self.numero1 // self.numero2

    def residuo(self):
        return self.numero1 % self.numero2

    def exponente(self):
        return self.numero1 ** self.numero2

    def mostrar(self):
        print("Operando 1 : {} , Operando 2 : {}".format(self.numero1,self.numero2))

print ("Menú de operaciones matematicas")
print("1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Division Entera\n6) Residuo\n7) Exponente\n8) Salir")

escoger="0"
n1,n2 = 0,0
while escoger != "8":
    escoger = input("Escoga una opcion [1...8]: ")
    if escoger == "0" or escoger == "8":
        pass
    else:
        n1 = int(input("Ingrese el numero 1 : "))
        n2 = int(input("Ingrese el numero 2 : "))
    op = Operaciones(n1,n2)

    if escoger == "1":
        print("{}+{}={}".format(op.numero1,op.numero2,op.suma()))
    elif escoger == "2":
        print("{}-{}={}".format(op.numero1, op.numero2, op.resta()))
    elif escoger == "3":
        print("{}*{}={}".format(op.numero1, op.numero2, op.multiplicacion()))
    elif escoger == "4":
        print("{}/{}={}".format(op.numero1, op.numero2, op.division()))
    elif escoger == "5":
        print("{}//{}={}".format(op.numero1, op.numero2, op.division_entera()))
    elif escoger == "6":
        print("{} mod {}={}".format(op.numero1, op.numero2, op.residuo()))
    elif escoger == "7":
        print("{}**{}={}".format(op.numero1, op.numero2, op.exponente()))
    elif escoger == "8":
        print("salir")
    else:
        print("Opcion no valida")
