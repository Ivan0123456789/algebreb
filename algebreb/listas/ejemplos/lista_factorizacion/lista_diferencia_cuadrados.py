from algebreb.listas.listas_factorizacion import ListaDiferenciaCuadrados
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a]
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 3
caracteristicas['cmin'] = 1
caracteristicas['cmax'] = 10

ldc = ListaDiferenciaCuadrados(caracteristicas)
json_object = json.dumps(ldc.as_str_latex(), indent=4)
print(json_object)