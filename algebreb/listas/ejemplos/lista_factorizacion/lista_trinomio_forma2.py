from algebreb.listas.listas_factorizacion import ListaTrinomioFormaII
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a]
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10 

ltf2 = ListaTrinomioFormaII(caracteristicas)
json_object = json.dumps(ltf2.as_str_latex(), indent=4)
print(json_object)