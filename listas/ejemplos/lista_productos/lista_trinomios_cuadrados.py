from algebreb.listas.listas_productos_notables import ListaTrinomioAlCuadrado
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [a, b, c]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = True
caracteristicas['gmin'] = 2 #Grado mínimo 2
caracteristicas['gmax'] = 3
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10

ltc = ListaTrinomioAlCuadrado(caracteristicas)
json_object = json.dumps(ltc.as_str_latex(), indent=4)
print(json_object)