class BASE_DATOS:
    def __init__(self):
     self.lista_animales = []
     
    def agregar_dato(self,nuevo):
        self.lista_animales.append(nuevo)
         
    def eliminar_dato(self,posicion):
        self.lista_animales.pop(posicion)     
        
    def mostrar_datos(self):
        for a in self.lista_animales:
            print("nombre:", a.nombre)
            print("edad:", a.edad)
            print("habitat:", a.habitat)
            print("dieta:", a.dieta)
            print("tamaño:", a.tamaño)
            print("color:", a.color) 
            print("------------------")
             
            
            
            
           
            
            
            