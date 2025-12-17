class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa
        self.grabados = grabados
        
    def contener_liquidos(self):
        return "la botella puede contener liquidos"
    
    def cierre_hermetico(self):
        return "la botella tiene cierre hermetico "
    
    def transporte(self):
        return "la botella se transporta con facilidad"
    
    def manejo(self):
        return "la botella es facil de sostener"
    
    def reutilizacion(self):
        return "la botella puede reutilizarse"