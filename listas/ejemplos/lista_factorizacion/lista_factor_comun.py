from algebreb.listas.listas_factorizacion import ListaFactorComun
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 1
caracteristicas['variables'] = [y]
caracteristicas['completo'] = True
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 3
caracteristicas['cmin'] = -20
caracteristicas['cmax'] = 10

lfc = ListaFactorComun(caracteristicas)
json_object = json.dumps(lfc.as_str_latex(), indent=4)
print(json_object)