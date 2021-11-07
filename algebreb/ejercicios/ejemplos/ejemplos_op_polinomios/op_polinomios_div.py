from algebreb.ejercicios.operaciones_polinomio import DivPolinomios
from algebreb.expresiones.polinomios import polinomio_coeficientes_aleatorios
from sympy.abc import x, y, z

# Ejemplo 1
# Multiplicacion de polinomios
# Polinomios completos de grado 2 y 3,con coeficientes enteros aleatorios en un rango de -10 a 10
# con variable independiente 'x'
p1 = polinomio_coeficientes_aleatorios(2, [x], 'ZZ', -10, 10, False, True)
p2 = polinomio_coeficientes_aleatorios(3, [x], 'ZZ', -10, 10, False, True)
div = DivPolinomios(p1, p2)

print(div.as_str())
print(div.as_latex())

# Ejemplo 2
# Multiplicacion de polinomios
# Polinomios incompletos de grado 2,con coeficientes enteros aleatorios en un rango de -100 a 100
# con variables independientes 'y' y 'z'
p3 = polinomio_coeficientes_aleatorios(2, [y, z], 'ZZ', -100, 100, False, False)
p4 = polinomio_coeficientes_aleatorios(2, [y, z], 'ZZ', -100, 100, False, False)
div = DivPolinomios(p3, p4)

print(div.as_str())
print(div.as_latex())

# Ejemplo 3
# Multiplicacion de polinomios
# Polinomios incompletos de grado 2 y 5,con coeficientes racionales aleatorios en un rango de -8 a 7
# con variable independiente 'y'
p5 = polinomio_coeficientes_aleatorios(2, [y], 'QQ', -8, 7, False, True)
p6 = polinomio_coeficientes_aleatorios(2, [y], 'QQ', -8, 7, False, True)
div = DivPolinomios(p5, p6)

print(div.as_str())
print(div.as_latex())

# Ejemplo 4
# Multiplicacion de polinomios
# Polinomios incompletos de grado 2 y 5,con coeficientes racionales fraccionarios aleatorios en un rango de -8 a 7
# con variables independientes 'x' y 'z'
p7 = polinomio_coeficientes_aleatorios(2, [x, z], 'QQ', -8, 7, True, True)
p8 = polinomio_coeficientes_aleatorios(3, [x, z], 'QQ', -8, 7, True, True)
div = DivPolinomios(p7, p8)

print(div.as_str())
print(div.as_latex())