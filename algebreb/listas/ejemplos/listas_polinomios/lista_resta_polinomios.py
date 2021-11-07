from algebreb.ejercicios.operaciones_polinomio import RestaPolinomios
from algebreb.listas.listas_polinomios import ListaRestaPolinomios
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

lrp = ListaRestaPolinomios(caracteristicas)
json_object = json.dumps(lrp.as_str_latex(), indent=4)
print(json_object)

