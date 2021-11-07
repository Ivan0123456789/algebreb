from algebreb.listas.listas_factorizacion import ListaCuboPerfectoBinomios
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 50
caracteristicas['variables'] = [a, b]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 3
caracteristicas['cmin'] = -100
caracteristicas['cmax'] = 50

lcpb = ListaCuboPerfectoBinomios(caracteristicas)
json_object = json.dumps(lcpb.as_str_latex(), indent=4)
print(json_object)
