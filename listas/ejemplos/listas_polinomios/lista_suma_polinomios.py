from algebreb.ejercicios.operaciones_polinomio import SumaPolinomios
from algebreb.listas.listas_polinomios import ListaSumaPolinomios
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 5
caracteristicas['variables'] = [a, b]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = True
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10
caracteristicas['completo'] = False

lsp = ListaSumaPolinomios(caracteristicas)
json_object = json.dumps(lsp.as_str_latex(), indent=4)
print(json_object)