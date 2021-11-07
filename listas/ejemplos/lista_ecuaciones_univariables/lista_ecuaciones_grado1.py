from algebreb.listas.listas_ecuaciones_univariables import ListaEcuacionesGrado1
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['cmin'] = 1
caracteristicas['cmax'] = 10

leg1 = ListaEcuacionesGrado1(caracteristicas)
print(leg1.as_str_latex())
json_object = json.dumps(leg1.as_str_latex(), indent=4)
print(json_object)