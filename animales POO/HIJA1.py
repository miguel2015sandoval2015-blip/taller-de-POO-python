from padre import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,velocidad):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.velocidad = velocidad
    def moverse(self):
        print(self.nombre, " el caballo galopa")
        
    def mostrar_extra(self):
        print("velocidad:",self.velocidad, "km/h")