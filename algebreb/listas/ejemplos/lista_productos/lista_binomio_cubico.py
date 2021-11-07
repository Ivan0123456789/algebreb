from algebreb.listas.listas_productos_notables import ListaBinomioAlCubo
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [a, b]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 2
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10

lbc = ListaBinomioAlCubo(caracteristicas)
json_object = json.dumps(lbc.as_str_latex(), indent=4)
print(json_object)