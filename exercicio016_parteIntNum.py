# Exercício 016 - Parte Inteira de um Número

n = float(input('Digite um número: '))

'''
#OPÇÃO 1 - USANDO A FUNÇÃO TRUNC
from math import trunc

print(f'A parte inteira do valor digitado é {trunc(n)}')
'''

#OPÇÃO 2 - USANDO A FUNÇÃO INT
print(f'A parte inteira de {n} é: {int(n)}')
