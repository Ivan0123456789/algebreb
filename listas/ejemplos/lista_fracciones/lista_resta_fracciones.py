from algebreb.listas.listas_fracciones_algebraicas import ListaRestaFraccionesAlgebraicas
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [x]
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2 
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10

lrfa = ListaRestaFraccionesAlgebraicas(caracteristicas)
json_object = json.dumps(lrfa.as_str_latex(), indent=4)
print(json_object)