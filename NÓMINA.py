from datetime import date

class Empresa:
    def __init__(self,id,dir,tel,nom,ruc):
        self.empleado = []
        self.__id = id
        self.departamento = []
        self.direccion = dir
        self.telefono = tel
        self.nombre = nom
        self.ruc = ruc
        

    def registrarEmpleado(self,nom,suel,fing,ced,corr,tel):
        empleado = Empleado(nom,suel,fing,ced,corr,tel)
        self.empleado.append(empleado.nombre)
    def mostrarEmpleado(self):
        print("EMPLEADOS: {}".format(",".join(self.empleado)))   
    def registrarDepartamento(self,des):
        dep = Departamento(des)
        self.departamento.append(dep)
    def mostrardEPARTAMAENTO(self):
        print("DEPARTAMENTOS: {}".format(",".join(self.departamento)))    
    def mostrarEmpresa(self):
        print("            ",self.nombre,"                ")
        print("DIRECCIÓN:",self.direccion,"               ")
        print("RUC: {} ID: {}".format(self.ruc,self.id))
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,nid):
        self.__id = nid
class Departamento:
    sec = 0
    def __init__(self,des,empleado=''):
        Departamento.sec += 1
        self.empleado = empleado
        self.__id = Departamento.sec
        self.descripcion = des
    
    def mostrarDep(self):
        print(self.id,self.descripcion)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,nid):
        self.__id = nid  
class Empleado:
    sec  = 0
    def __init__(self,nom,suel,fing,ced,corr,tel):
        Empleado.sec += 1
        self.__id = Empleado.sec
        self.nombre = nom
        self.sueldo = suel
        self.fechaingreso = fing
        self.cedula = ced
        self.telefono = tel
        self.correo = corr  
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,nid):
        self.__id = nid
class Obrero(Empleado):
    def __init__(self,nom, suel, fing, ced, corr, tel,sind=True,cont=True):
        super().__init__(nom, suel, fing, ced, corr, tel)
        self.sindicato = sind
        self.contratocolectivo = cont
class Administrativo(Empleado):
    def __init__(self,nom, suel, fing, ced, corr, tel, com=True):
        super().__init__(nom, suel, fing, ced, corr, tel)
        self.comision = com
class Prestamos:
    sec = 0
    def __init__(self,fec,val,numpag,empleado,est=True):
        Prestamos.sec+=1
        self.__id = Prestamos.sec
        self.fecha = fec
        self.valor = val
        self.numpagos = numpag
        self.cuotas = 0
        self.empleado = empleado
        self.saldo = self.valor
        self.estado = est
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor
    
    def calcular(self):
        if self.estado == True:
            self.cuotas = self.valor / self.numpagos
            self.saldo -=self.cuotas
            return self.cuotas , self.saldo    
    def mostrarPrestamo(self):
        self.calcular()
        print('ID : {}  Empleado : {}   Valor: {}  Numero pagos: {}  Cuotas: {:.2f}  Saldo: {:.2f}'.format(self.id,self.empleado.nombre,self.valor,self.numpagos,self.cuotas,self.saldo) )
class Sobretiempo:
    sec = 0
    def __init__(self,hrec,hext,emp,fec,estado=True):
        Sobretiempo.sec += 1 
        self.__id = Sobretiempo.sec
        self.horarecargo = hrec
        self.horasextraordianria = hext
        self.empleado = emp
        self.fecha = fec
        self.estado = estado
    
    def calculo(self):
        if self.estado==True:
            valor = self.empleado.sueldo/240
            sobretiempo = valor * ((self.horarecargo*0.50)+(self.horasextraordianria*2))
            return sobretiempo
        else:
            sobretiempo = 0
            return sobretiempo

    def mostrar(self):
        cal = self.calculo()
        print('ID :{}      Empleado :{}    Sobretiempo:{}'.format(self.id,self.empleado.nombre,cal))

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor      
class Deducciones:
    sec = 0
    def __init__(self,com=0,anti=0):
        Deducciones.sec +=1
        self.__id = Deducciones.sec
        self.iess = 0.1115
        self.comision = com
        self.antiguedad = anti

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor
    
    def mostrarDeducciones(self):
        print('ID:{}     IEES:{}    Comision:{}   Antiguedad:{}'.format(self.id,self.iess,self.comision,self.antiguedad))
class Nomina:
    sec =0
    def __init__(self,empleado,fecha,sobretiempo,prestamo):
        Nomina.sec += 1
        self.__id = Nomina.sec
        self.empleado = empleado
        self.fecha=fecha
        self.sueldo = self.empleado.sueldo
        self.sobretiempo = sobretiempo
        self.prestamo = prestamo    
    def calculos(self,iess,comision=0,antiguedad=0):

        self.comisionemp = comision * self.sueldo
        self.antiguedad = antiguedad*((self.fecha - self.empleado.fechaingreso).days)/365*self.sueldo
        self.Empleadoiess = iess*self.empleado.sueldo
        self.totingresos = self.sueldo + self.sobretiempo.calculo()  +  self.comisionemp + self.antiguedad 
        self.prestamo.calcular()
        self.totdes = self.Empleadoiess + self.prestamo.cuotas
        self.liquido = self.totingresos - self.totdes
        return self.totingresos , self.totdes , self.Empleadoiess , self.liquido , self.comisionemp , self.antiguedad
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor            
    def mostrarNomina(self):
        print(' _____________________________________________________________')
        print("|         EMPRESA DE COMIDA RÁPIDA      |     ID: {}       |".format(empresa.id))
        print('|------------------------------------------------------------|')
        print("|    Empresa {}    |     RUC:{}      |".format(empresa.nombre,empresa.ruc))
        print('|------------------------------------------------------------|')
        print("| DIRECCIÓN:{}   |    EMPLEADOS: {}    |".format(empresa.direccion,len(empresa.empleado)))
        print('|------------------------------------------------------------|')
        print('|------------------------------------------------------------|')
        print('|                          NOMINA                            |')
        print('|------------------------------------------------------------|')
        print('|       TRABAJADOR      |         DNI         |      ID      |')
        print('|------------------------------------------------------------|')
        print("|     {}  |      {}     |      {}       |".format(self.empleado.nombre,self.empleado.cedula,self.empleado.id))
        print('|------------------------------------------------------------|')
        print("|    FECHA DE INGRESO   |     DEPARTAMENTO    |     CLASE    |")
        print('|------------------------------------------------------------|')
        print("|       {}      |     Departamento    | obrero/admin |".format(self.empleado.fechaingreso))
        print('|------------------------------------------------------------|')

        print('|____________________________________________________________|')        
        print("|     PERÍODO DEVENGADO         |         Fecha de cobro     |")
        print('|------------------------------------------------------------|')
        print('|    Del 0 al 31 de Agosto      |          {}        |'.format(self.fecha))
        print('|------------------------------------------------------------|')
        print('|------------------------------------------------------------|')
        print('|       CONCEPTO      |      DEVENGO        |    DEDUCCION   |')
        print('|------------------------------------------------------------|')
        print('|      Sueldo         |       $ {}         |                |'.format(self.sueldo))
        print('|      Sobretiempo    |       $ {}        |                |'.format(self.sobretiempo.calculo()))
        print('|      Comision       |       $ {}        |                |'.format(self.comisionemp))        
        print('|      Antiguedad     |       $ {:.2f}        |                |'.format(self.antiguedad))         
        self.prestamo.calcular()
        print('|      Prestamo       |                     |     $ {:.2f}    |'.format(self.prestamo.cuotas))
        print('|      IEES           |                     |     $ {:.2f}    |'.format(self.Empleadoiess))
        print('|------------------------------------------------------------|')
        print('|------------------------------------------------------------|')
        print("|         TOTAL DEVENGO        |       TOTAL DEDUCCIONES     |")
        print('|------------------------------------------------------------|')
        print('|         $  {:.2f}           |        $ {:.2f}             |'.format(self.totingresos,self.totdes))
        print('|------------------------------------------------------------|')
        print('|------------------------------------------------------------|')
        print("|                  LÍQUIDO TOTAL A RECIBIR                   |")
        print('|------------------------------------------------------------|')
        print('|                         $ {:.2f}                          |'.format(self.liquido))
        print('|____________________________________________________________|') 
        print("\n \n")

today = date.today()
empresa=Empresa(4050,"Av. 8 Abril y Carlos AMEN",454545,"LOS POLLOS HERMANOS S.A","#1449")
empleado1 = Empleado('Josue Cozzarelli',800,date(2021,9,4),'0928151432','jcozarellij@unemi.edu.ec','0959788523')
empleado2 = Administrativo('Luis Bonilla Rey',700,date(2019,11,25),'0928175223','lbonillar@unemi.edu.ec','0990822011')
empresa.registrarEmpleado(empleado1.nombre,empleado1.sueldo,empleado1.fechaingreso,empleado1.cedula,empleado1.correo,empleado1.telefono)
empresa.registrarEmpleado(empleado2.nombre,empleado2.sueldo,empleado2.fechaingreso,empleado2.cedula,empleado2.correo,empleado2.telefono)
prestamo1 = Prestamos(today,800,12,empleado1,True)
deduccion1= Deducciones(2,0)
extra1 = Sobretiempo(4,8,empleado1,today,True)
extra1.calculo()
nomina1 = Nomina(empleado1,today,extra1,prestamo1)
nomina1.calculos(deduccion1.iess,deduccion1.comision,deduccion1.antiguedad)
nomina1.mostrarNomina()
prestamo2= Prestamos(today,800,12,empleado2,True)
deduccion2= Deducciones(2,0)
extra2 = Sobretiempo(4,8,empleado2,today,True)
extra2.calculo()
nomina2= Nomina(empleado2,today,extra2,prestamo2)
nomina2.calculos(deduccion1.iess,deduccion1.comision,deduccion1.antiguedad)
nomina2.mostrarNomina()

