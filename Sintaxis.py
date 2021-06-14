#sintaxis

#num = 20
#if type(num) == int:
#     print("respuesta:",num*2)
# else:
#     print("El dato no es numerico")
#
# def mensaje(men):
#     print(men)
#
# mensaje("Mi primer programa")
# mensaje("Mi segundo programa")

class Usuario:
    instancia = 0 #variable de clase (opcional)
    #_init_Metodo constructor que se ejecutaq cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que representa la clase creada.
    def __init__(self,palabra="Bienvenido"):
        self.Texto = palabra # variable de instancia
        #Sintaxis.instancia = Sintaxis.instancia+1

    def useVariable(self):
        edad, _peso = 29 , 63.50
        nombre = 'Loenidas Chávez'
        Tipo_sexo = 'M'
        civil = True
        #tuplas = () son colecciones de datos de cualquier tipo inmutable 
        us = ('llqchavez', '0611' ,'llqchavez@gmail.com', True)
        #usuario[3] = "milagro"
        # listas = [] colecciones multiples
        materias = []
        materias = ['Programación Web','Algoritmo','IA'] 
        materias[1] = "Python"
        materias.append("Go")
        #diccionario ={} colcecciones de objetos clave:valor tipo json
        profesor = {}
        profesor = {'Nombre':'Leonidas','Edad':29,'Facultad': 'Faci'}
         #Imprimir
        print("""Mi nombre es {}, tengo {} años""".format(nombre,edad))
        print(us,materias,profesor)

        us = ('llqchavez','0611','llqchavez@gmail.com')
        #usuario[3] = "milagro"
        # listas = [] colecciones multiples
        materias = []
        materias = ['Programación Web','Algoritmo','IA'] 
        materias[1] = "Python"
        materias.append("Go")
        #diccionario ={} colcecciones de objetos clave:valor tipo json
        profesor = {}
        profesor = {'Nombre':'Leonidas','Edad':29,'Facultad': 'Faci'}
         #Imprimir
        print("""Mi nombre es {}, tengo {} años""".format(nombre,edad))
        print(us,materias,profesor)
        print(nombre,edad)

persona = Usuario() #se crea un objeto que es una instancia de la clase
persona.useVariable()
print(persona.Texto)