from algebreb.ejercicios.operaciones_polinomio import TermPolinomio
from algebreb.expresiones.polinomios import polinomio_coeficientes_aleatorios
from sympy.abc import x, y, z

# Ejemplo 1
# Suma de polinomios
# Polinomios completos de grado 2 y 3,con coeficientes enteros aleatorios en un rango de -10 a 10
# con variable independiente 'x'
p1 = polinomio_coeficientes_aleatorios(1, [x], 'ZZ', -10, 10, False, True)
termino = TermPolinomio(p1)

print(termino.as_str())
print(termino.as_latex())