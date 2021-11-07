from algebreb.listas.listas_factorizacion import ListaTrinomioCuadradoPerfecto
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = True
caracteristicas['completo'] = True
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 3
caracteristicas['cmin'] = 1
caracteristicas['cmax'] = 10

ltcp = ListaTrinomioCuadradoPerfecto(caracteristicas)
json_object = json.dumps(ltcp.as_str_latex(), indent=4)
print(json_object)
num = 4
print(num.denominator)