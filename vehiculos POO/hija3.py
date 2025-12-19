from padre import vehiculo

class volqueta(vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible,capacidad_carga):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.capacidad_carga = capacidad_carga
        
    def cargar_material(self):
        print(self.modelo , "esta cargando material. capacidad" + self.capacidad_carga, "toneladas")
        
    def descargar_material(self):

        print(self.modelo, "descarga material")  

    def mostrar_extra(self):
        print("capacidad de carga:", self.capacidad_carga, "toneladas")
