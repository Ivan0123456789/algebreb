from algebreb.listas.listas_ecuaciones_univariables import ListaEcuacionesGrado2
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [a]
caracteristicas['dominio'] = 'QQ'
caracteristicas['fraccion'] = True
caracteristicas['cmin'] = 1
caracteristicas['cmax'] = 10

leg2 = ListaEcuacionesGrado2(caracteristicas)
print(leg2.as_str_latex())
json_object = json.dumps(leg2.as_str_latex(), indent=4)
print(json_object)