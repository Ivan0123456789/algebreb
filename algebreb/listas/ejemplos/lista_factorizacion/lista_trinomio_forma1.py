from algebreb.listas.listas_factorizacion import ListaTrinomioFormaI
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [a]
caracteristicas['cmin'] = -100
caracteristicas['cmax'] = 10

ltf1 = ListaTrinomioFormaI(caracteristicas)
json_object = json.dumps(ltf1.as_str_latex(), indent=4)
print(json_object)

