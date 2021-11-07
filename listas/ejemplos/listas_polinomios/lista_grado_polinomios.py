from algebreb.ejercicios.operaciones_polinomio import GradoPolinomio
from algebreb.listas.listas_polinomios import ListaGradoPolinomios
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a, b]
caracteristicas['dominio'] = 'QQ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10
caracteristicas['completo'] = False

lsp = ListaGradoPolinomios(caracteristicas)
json_object = json.dumps(lsp.as_str_latex(), indent=4)
print(json_object)