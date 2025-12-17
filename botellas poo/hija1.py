#crear la clase 
from padre import Botella


class BotellaPlastica(Botella):
    #1.crear el contructor
    def __init__(self,capacidad,forma,diseño,tapa,grabados):
        #3. crear atributos
        super().__init__(material="plastico",capacidad=capacidad,forma=forma,diseño=diseño,tapa=tapa,grabados=grabados)
    
    def transparencia(self):
        return "la botella platica es transparente"
    
    def compatibilidad_bebidad(self):
        return "la botella es apta para bebidas frias"