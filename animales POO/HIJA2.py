from padre import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,longitud):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.longitud = longitud
        
    def moverse(self):
        print(self.nombre, "se mueve nadando y caminado")
        
    def mostrar_extra(self):
        print("longitud:", self.longitud, "m")        