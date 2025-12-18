# CREAR CLASE
from  padre import vehiculo

class AutoDeportivo(vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        
    def activar_turbo(self):
        print(self.modelo + " se activa el turbo")
        
    def activar_modo_deportivo(self):
        print(self.modelo + "se activa el modo deportivo")        