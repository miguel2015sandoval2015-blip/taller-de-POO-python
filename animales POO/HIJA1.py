from padre import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)