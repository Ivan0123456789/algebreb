from algebreb.listas.listas_productos_notables import ListaBinomiosFormaII
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [a]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10

lbf2 = ListaBinomiosFormaII(caracteristicas)
json_object = json.dumps(lbf2.as_str_latex(), indent=4)
print(json_object)