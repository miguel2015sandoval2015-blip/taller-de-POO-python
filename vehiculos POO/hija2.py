from padre import vehiculo
class Camioneta(vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        
    def remolcar(self):
        print(self.modelo + "remolca otro vehiculo") 
        
    def activar4x4(self):
        print(self.modelo + "activa el 4x4")       