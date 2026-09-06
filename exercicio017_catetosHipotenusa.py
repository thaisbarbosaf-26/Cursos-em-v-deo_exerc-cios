co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

'''
#OPÇÃO 1 - RESOLVENDO USANDO A FÓRMULA DE PITÁGORAS
hipot = (co ** 2 + ca ** 2) ** (1/2)

print(f' A hipotenusa vai medir {hipot:.2f}')

'''

'''
#OPÇÃO 2 - RESOLVENDO USANDO A BIBLIOTECA MATH

import math

hi = math.hypot(co, ca)

print(f'A hipotenusa vai medir {hi:.2f}')

'''

#OPÇÃO 3 - C/ BIBLIOTECA MATH E FUNÇÃO HYPOT

from math import hypot

hi = hypot(co,ca)

print(f'A hipotenusa vai medir {hi:.2f}')

