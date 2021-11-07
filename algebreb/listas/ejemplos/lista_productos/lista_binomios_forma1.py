from algebreb.listas.listas_productos_notables import ListaBinomiosFormaI
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [a]
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10

lbf1 = ListaBinomiosFormaI(caracteristicas)
json_object = json.dumps(lbf1.as_str_latex(), indent=4)
print(json_object)