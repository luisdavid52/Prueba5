from cargos import Cargo
class empleado:
    secuencia=0
    def __init__(self,nom,ced,sue,cargo):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargo
    def mostrar(self):
        print("codigo: {} nombre: {} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))
    def generarCodigo(self):
        empleado.secuencia=empleado.secuencia+1
        return empleado.secuencia
cargo1=Cargo("Docente")
emp1=empleado("Luis","0952",500,cargo1)
emp1.mostrar()
cargo2=Cargo("Analista")
emp2=empleado("Ana","0914",cargo2)
emp2.mostrar()