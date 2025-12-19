from padre import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,tipo_agua):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua
        
    def moverse(self):
        print(self.nombre, "se mueve nadando en agua", self.tipo_agua)
        
    def mostrar_extra(self):
        print("tipo de agua", self.tipo_agua)
            
        