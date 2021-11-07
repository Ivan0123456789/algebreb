from algebreb.listas.listas_productos_notables import ListaBinomioAlCuadrado
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [x, y]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1 
caracteristicas['gmax'] = 3
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10

lbc = ListaBinomioAlCuadrado(caracteristicas)
json_object = json.dumps(lbc.as_str_latex(), indent=4)
print(json_object)
print(type(json_object))