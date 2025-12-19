from padre import Animal

class pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,tipo_pico):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_pico = tipo_pico
        
    def moverse(self):
        print(self.nombre, "se mueve nadando o caminado y volando")
        
    def mostrar_extra(self):
        print("tipo de pico:", self.tipo_pico)
               