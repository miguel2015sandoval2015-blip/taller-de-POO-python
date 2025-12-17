class BaseDatos:
    def __init__(self):
        self.lista_botellas =[]
        
    def agregar_dato(self, nuevo):
        self.lista_botellas.append(nuevo)
        
    def eliminar_dato(self, posicion):
        self.lista_botellas.pop(posicion)
        
   
    def mostrar_datos(self):
        for b in self.lista_botellas:
            print("material: ", b.material) 
            print("capacidad: ", b.capacidad)
            print("forma", b.forma)
            print("diseño", b.diseño)
            print("tapa", b.tapa)
            print("grabados", b.grabados)         
            print("----------------------")