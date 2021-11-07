from algebreb.listas.listas_productos_notables import ListaBinomiosConjugados
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 1
caracteristicas['variables'] = [a, b]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10

lbc = ListaBinomiosConjugados(caracteristicas)
json_object = json.dumps(lbc.as_str_latex(), indent=4)
print(json_object)