from padre import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,especie):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.especie = especie

    def moverse(self):
        print(self.nombre, " se mueve volando o caminado")
        
    def mostrar_extra(self):
        print("especie: ", self.especie)
        
            