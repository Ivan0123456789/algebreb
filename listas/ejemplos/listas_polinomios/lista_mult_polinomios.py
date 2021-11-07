from algebreb.ejercicios.operaciones_polinomio import MultPolinomios
from algebreb.listas.listas_polinomios import ListaMultPolinomios
from sympy.abc import a, b, c, x, y , z
import json

caracteristicas = {}
caracteristicas['cantidad'] = 10
caracteristicas['variables'] = [a, b]
caracteristicas['dominio'] = 'ZZ'
caracteristicas['fraccion'] = False
caracteristicas['gmin'] = 1
caracteristicas['gmax'] = 2
caracteristicas['cmin'] = -10
caracteristicas['cmax'] = 10
caracteristicas['completo'] = True

lmp = ListaMultPolinomios(caracteristicas)
json_object = json.dumps(lmp.as_str_latex(), indent=4)
print(json_object)

