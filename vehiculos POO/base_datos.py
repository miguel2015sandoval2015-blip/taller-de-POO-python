from hija3 import volqueta
class BaseDatos:
    def __init__(self):
        self.lista_vehiculos = []
        
    def agregar_dato(self, nuevo):
        self.lista_vehiculos.append(nuevo)
        
    def eliminar_dato(self, posicion):
        self.lista_vehiculos.pop(posicion)
        
    def mostrar_datos(self):
        for v in self.lista_vehiculos:
            print("modelo: ", v.modelo)
            print("color: ", v.color)
            print("motor: ", v.motor) 
            print("puertas: ", v.puertas)
            print("pasajeros: ", v.pasajeros)
            print("combustible: ", v.combustible) 
            
            
            v.mostrar_extra()          
            

            print("------------------")    
