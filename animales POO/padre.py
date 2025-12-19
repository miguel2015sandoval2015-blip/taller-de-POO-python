class Animal:
    def __init__(self,nombre,edad,habitat,dieta,tamaño,color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color
        
    def moverse(self):
        print(self.nombre, "se esta moviendo.")
        
    def comunicacion(self):
        print(self.nombre, "se esta comunicando.")
        
    def reproduccion(self):
        print(self.nombre, "se esta reproducciendo")
        
    def alimentacion(self):
        print(self.nombre, "se esta alimentado.")
        
    def adaptacion(self):
        print(self.nombre, "se esta adaptando en su nuevo habitat.")
        
    def instintos(self):
        print(self.nombre, "actua segun sus instintos")                       
    
    def descanso (self):
        print(self.nombre, "esta descansando.")
        
    def sueño(self):
        print(self.nombre, "esta durmiendo")
        
    def interaccion_social(self):
        print(self.nombre, "interactuara con los de su especie") 
                   