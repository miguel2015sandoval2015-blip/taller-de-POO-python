class vehiculo :
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        self.pasajeros = pasajeros
        self.combustible = combustible
        
    def arrancar_vehiculo(self):
        print (self.modelo + "el vehiculo puede arrancar")
    
    def apagar_vehiculo(self):
        print (self.modelo + "el vehiculo puede apagarse") 
        
    def acelerar_frenado(self):
        print (self.modelo + "el vehiculo puede acelerar y frenar") 
        
    def direccion(self):
        print (self.modelo + "el vehiculo puede dar direccion") 
        
    def climatizacion(self):
        print (self.modelo + "el vehiculo tiene A/C")
        
    def seguridad(self):
        print (self.modelo + "tiene sistema de seguridad")
        
    def luces(self):
        print (self.modelo + "se pueden encender las luces")
        
    def ventanas(self):
        print (self.modelo + "tiene sistema de ventanas")
        
    def espejos(self):
        print (self.modelo + "los espejos estan operativos")                             
        
    def mostrar_extra(self):
        print("capidad de carga")    