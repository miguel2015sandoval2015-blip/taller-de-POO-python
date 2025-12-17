from padre import Botella

class BotellaVidrio(Botella):
    def __init__(self,capacidad,forma,diseño,tapa,grabados):
        super().__init__(material = "vidrio",capacidad=capacidad,forma=forma,diseño=diseño,tapa=tapa,grabados=grabados)
    
    def transparencia(self):
        return "la botella de vidrio puede ser transparente o oscura"
            
    def compatibilidad_bebidas(self):
        return "la botella de vidrio es apta para bebidas frias o calientes"    
        