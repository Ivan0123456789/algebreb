from algebreb.ejercicios.operaciones_polinomio import MultPolinomios
from algebreb.listas.listas_polinomios import ListaDivPolinomios
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10
caracteristicas['completo'] = True
caracteristicas['exacta'] = False

ldp = ListaDivPolinomios(caracteristicas)
json_object = json.dumps(ldp.as_str_latex(), indent=4)
print(json_object)

