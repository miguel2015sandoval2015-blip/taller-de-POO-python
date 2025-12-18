from hija1 import AutoDeportivo
from hija2 import Camioneta
from hija3 import volqueta
from base_datos import BaseDatos

bd = BaseDatos()

v1 = AutoDeportivo("Mustang GT", "negro", "V8",2,2, "gasolina")
v2 = Camioneta("Ford", "azul", "6 cilindros",4,5,"diesel")
v3 = volqueta("Dodge","verde","ISX", 2,3, "diesel", 18)

bd.agregar_dato(v1)
bd.agregar_dato(v2)
bd.agregar_dato(v3)

bd.mostrar_datos()

bd.eliminar_dato(1)
