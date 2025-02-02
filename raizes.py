'''
Faça um programa principal em Python que encontre
as raízes da equação ax2 + bx + c usando a
fórmula de Baskara. Os valores de a, b e c devem
ser introduzidos pelo usuário no teclado. Entre com
a=2, b=4 e c=-3, para que o delta seja positivo.
'''

import math

def delta(a, b, c):
    return b**2 - 4*a*c



a=2
b=4
c=-3
d = delta(a,b,c)

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)


print(x1,x2)
