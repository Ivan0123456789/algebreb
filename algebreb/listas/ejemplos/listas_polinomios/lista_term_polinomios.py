from algebreb.listas.listas_polinomios import ListaTermPolinomio
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a]
caracteristicas['dominio'] = 'QQ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10
caracteristicas['completo'] = False

lsp = ListaTermPolinomio(caracteristicas)
json_object = json.dumps(lsp.as_str_latex(), indent=4)
print(json_object)