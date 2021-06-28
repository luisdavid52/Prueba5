class Cargo:
    secuencia=0
    def __init__(self,des="Sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia
        self.descripcion=des
cargo1=Cargo()
print(cargo1.codigo,cargo1.descripcion)
cargo2=Cargo()
cargo2.descripcion="Director"
print(cargo2.codigo,cargo2.descripcion) 
cargo3=Cargo("Analista")
print(cargo3.codigo,cargo3.descripcion)    

    