from hija1 import BotellaPlastica
from hija2 import BotellaVidrio
from basedeDatos import BaseDatos

bd = BaseDatos()

b1 = BotellaPlastica("600 ml ", "cilindrica ", "transpararente ", "rosca ", "marca ")
b2 = BotellaVidrio("1 litro ", "recta", "oscura ", "corcho ", "sin grabados ")

bd.agregar_dato(b1)
bd.agregar_dato(b2)

bd.mostrar_datos()

bd.eliminar_dato(0)

bd.mostrar_datos()