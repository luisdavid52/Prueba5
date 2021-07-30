class Menu:
    def _init_(self, titulo, opciones=[]):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input('Elija opcion [1...{}]: '.format(len(self.opciones)))
        return opc

opc = ''
while opc != '5':
    menu = Menu('MENU PRINCIPAL', ['1) Calculadora', '2) Operacion numeros', '3) Tratamiento de listas', '4) Operacion de cadenas', '5) Salir'])
    opc = menu.menu()

    if opc == '1':
        opc1 = ''
        while opc1 != '10':
            menu1 = Menu('//--MENU CALCULADORA--//', ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) valor absoluto', '7) circunferencia', '8) area circulo','9) Area cuadrado', '10) Salir'])
            opc1 = menu1.menu()
    elif opc == '2':
        opc1 = ''
        while opc1 != '10':
            menu1 = Menu('//--MENU CALCULADORA--//', ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) valor absoluto', '7) circunferencia', '8) area circulo','9) Area cuadrado', '10) Salir'])
            opc1 = menu1.menu()
    elif opc == '3':
        opc1 = ''
        while opc1 != '10':
            menu1 = Menu('//--MENU CALCULADORA--//', ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) valor absoluto', '7) circunferencia', '8) area circulo','9) Area cuadrado', '10) Salir'])
            opc1 = menu1.menu()    
    elif opc == '4':
        opc1 = ''
        while opc1 != '10':
            menu1 = Menu('//--MENU CADENA--//', ['1) Suma', '2) Resta', '3) Multiplicacion', '4) Division', '5) Exponente', '6) valor absoluto', '7) circunferencia', '8) area circulo','9) Area cuadrado', '10) Salir'])
            opc1 = menu1.menu()

