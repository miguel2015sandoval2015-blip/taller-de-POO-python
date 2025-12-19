from HIJA1 import Caballo
from HIJA2 import Cocodrilo
from HIJA3 import Pez
from HIJA4 import Escarabajo
from HIJA5 import pato
from BAse_datos import BASE_DATOS

bd = BASE_DATOS()

a1 = Caballo("caballo criollo", 5, "potrero", "herbivoro", "grande", "marron")
a2 = Cocodrilo("cocodrilo del llano", 12, "llanura", "carnivoro", "grande","verde")
a3 = Pez("pez payaso",2,"oceano","omnivoro","pequeño","naranja")
a4 = Escarabajo("escarabajo rinoceronte", 1,"bosque", "detritivo", "pequeño","negro")
a5 = pato("pato criollo",3,"lago","omnivoro","mediano","blanco")

bd.agregar_dato(a1)
bd.agregar_dato(a2)
bd.agregar_dato(a3)
bd.agregar_dato(a4)
bd.agregar_dato(a5)

bd.mostrar_datos()

bd.eliminar_dato(1)