from algebreb.listas.listas_fracciones_algebraicas import ListaSimpFraccionesAlgebraicas
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [x] 
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 3

lsfa = ListaSimpFraccionesAlgebraicas(caracteristicas)
json_object = json.dumps(lsfa.as_str_latex(), indent=4)
print(json_object)